import uuid
import os
import tempfile
from datetime import datetime
from typing import List
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from parsers.file_parser import parse_file
from chains.pipeline import run_pipeline
from app.schemas import JobCreate, JobResponse, CandidateResult, ResultsResponse

app = FastAPI(title="Resume Screener API", version="1.0.0")

# CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
jobs_store = {}  # {job_id: {"id": ..., "title": ..., "description": ..., "created_at": ...}}
candidates_store = {}  # {candidate_id: {"id": ..., "job_id": ..., "filename": ..., "score": ..., etc}}

@app.get("/")
def root():
    return {"message": "Resume Screener API", "docs": "/docs"}

@app.post("/api/jobs", response_model=JobResponse)
def create_job(job: JobCreate):
    job_id = str(uuid.uuid4())
    job_data = {
        "id": job_id,
        "title": job.title,
        "description": job.description,
        "created_at": datetime.now().isoformat()
    }
    jobs_store[job_id] = job_data
    return JobResponse(**job_data)

@app.post("/api/jobs/{job_id}/resumes")
async def upload_resumes(job_id: str, files: List[UploadFile] = File(...)):
    if job_id not in jobs_store:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs_store[job_id]
    results = []
    
    for file in files:
        # Validate file extension
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in [".pdf", ".docx", ".txt"]:
            results.append({"filename": file.filename, "error": f"Unsupported format: {ext}"})
            continue
        
        # Save to temp file, parse, then delete
        try:
            content = await file.read()
            if len(content) == 0:
                results.append({"filename": file.filename, "error": "Empty file"})
                continue
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                tmp.write(content)
                tmp_path = tmp.name
            
            # Parse the file
            raw_text = parse_file(tmp_path)
            os.unlink(tmp_path)  # clean up
            
            if not raw_text.strip():
                results.append({"filename": file.filename, "error": "No text extracted"})
                continue
            
            # Run the LCEL pipeline
            evaluation = run_pipeline(raw_text, job["description"])
            
            candidate_id = str(uuid.uuid4())
            candidate_data = {
                "id": candidate_id,
                "job_id": job_id,
                "filename": file.filename,
                "score": evaluation.score,
                "matched_skills": evaluation.matched_skills,
                "missing_skills": evaluation.missing_skills,
                "reasoning": evaluation.reasoning
            }
            candidates_store[candidate_id] = candidate_data
            results.append(candidate_data)
            
        except Exception as e:
            results.append({"filename": file.filename, "error": str(e)})
    
    return {"job_id": job_id, "results": results}

@app.get("/api/jobs/{job_id}/results", response_model=ResultsResponse)
def get_results(job_id: str):
    if job_id not in jobs_store:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job = jobs_store[job_id]
    job_candidates = [
        CandidateResult(**c) for c in candidates_store.values()
        if c["job_id"] == job_id
    ]
    # Sort by score descending
    job_candidates.sort(key=lambda x: x.score, reverse=True)
    
    return ResultsResponse(
        job_id=job_id,
        job_title=job["title"],
        candidates=job_candidates
    )

@app.get("/api/candidates/{candidate_id}", response_model=CandidateResult)
def get_candidate(candidate_id: str):
    if candidate_id not in candidates_store:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return CandidateResult(**candidates_store[candidate_id])

@app.get("/api/jobs")
def list_jobs():
    return list(jobs_store.values())
