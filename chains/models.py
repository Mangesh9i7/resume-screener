from typing import List
from pydantic import BaseModel, Field

class ResumeSkills(BaseModel):
    technical_skills: List[str] = Field(description="List of technical skills explicitly mentioned in the resume")
    soft_skills: List[str] = Field(description="List of soft skills explicitly mentioned in the resume")
    years_experience: str = Field(description="Total years of experience")
    education: str = Field(description="Highest education degree or qualification")

class JobRequirements(BaseModel):
    required_skills: List[str] = Field(description="List of explicitly required skills for the job")
    nice_to_have: List[str] = Field(description="List of nice-to-have or optional skills for the job")
    min_experience: str = Field(description="Minimum years of experience required")

class EvaluationResult(BaseModel):
    score: int = Field(description="Score from 0 to 100 based on alignment between resume and job requirements")
    matched_skills: List[str] = Field(description="List of skills that are present in both the resume and job requirements")
    missing_skills: List[str] = Field(description="List of required skills missing from the resume")
    reasoning: str = Field(description="Detailed reasoning for the score and evaluation")
