from pydantic import BaseModel, Field
from typing import List

class ExtractedInfo(BaseModel):
    skills: List[str] = Field(description="List of technical and soft skills found in the resume")
    experience: str = Field(description="Summary of work experience and years")
    tools: List[str] = Field(description="List of software/tools found in the resume")

class EvaluationResult(BaseModel):
    score: int = Field(description="Fit score from 0 to 100 based strictly on the job requirements")
    explanation: str = Field(description="Detailed explanation of the score. Mention what matched and what is missing.")