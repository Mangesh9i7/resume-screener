import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from chains.models import ResumeSkills, JobRequirements, EvaluationResult
from prompts.templates import RESUME_EXTRACTION_PROMPT, JOB_EXTRACTION_PROMPT, EVALUATION_PROMPT

def get_llm():
    return ChatOpenAI(
        model=os.getenv("LLM_MODEL", "openai/gpt-4o-mini"),
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "Resume Screener"
        }
    )

def extract_resume_skills(resume_text: str) -> ResumeSkills:
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=ResumeSkills)
    prompt = ChatPromptTemplate.from_template(RESUME_EXTRACTION_PROMPT)
    chain = prompt | llm | parser
    return chain.invoke({"resume_text": resume_text, "format_instructions": parser.get_format_instructions()})

def extract_job_requirements(jd_text: str) -> JobRequirements:
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=JobRequirements)
    prompt = ChatPromptTemplate.from_template(JOB_EXTRACTION_PROMPT)
    chain = prompt | llm | parser
    return chain.invoke({"jd_text": jd_text, "format_instructions": parser.get_format_instructions()})

def evaluate_candidate(resume_skills: ResumeSkills, job_requirements: JobRequirements) -> EvaluationResult:
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=EvaluationResult)
    prompt = ChatPromptTemplate.from_template(EVALUATION_PROMPT)
    chain = prompt | llm | parser
    return chain.invoke({
        "resume_skills": resume_skills.model_dump_json(),
        "job_requirements": job_requirements.model_dump_json(),
        "format_instructions": parser.get_format_instructions()
    })

def run_pipeline(resume_text: str, jd_text: str) -> EvaluationResult:
    print("Extracting resume skills...")
    resume_skills = extract_resume_skills(resume_text)
    print(f"Found skills: {resume_skills.technical_skills}")
    print("Extracting job requirements...")
    job_requirements = extract_job_requirements(jd_text)
    print(f"Required: {job_requirements.required_skills}")
    print("Evaluating candidate...")
    evaluation = evaluate_candidate(resume_skills, job_requirements)
    return evaluation
