from typing import List
from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str

class JobResponse(BaseModel):
    id: str
    title: str
    description: str
    created_at: str

class CandidateResult(BaseModel):
    id: str
    filename: str
    score: int
    matched_skills: List[str]
    missing_skills: List[str]
    reasoning: str

class ResultsResponse(BaseModel):
    job_id: str
    job_title: str
    candidates: List[CandidateResult]
