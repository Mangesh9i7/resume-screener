RESUME_EXTRACTION_PROMPT = """You are an expert resume parser. Extract structured information from the following resume.

IMPORTANT RULES:
- Only extract skills that are EXPLICITLY mentioned in the resume
- Do NOT infer or assume skills that aren't stated
- If a skill category has no entries, return an empty list
- Be precise with years of experience - use exact numbers if stated
- For education, extract the highest degree mentioned

Resume:
{resume_text}

{format_instructions}
"""

JOB_EXTRACTION_PROMPT = """You are an expert job description analyzer. Extract the key requirements from this job posting.

IMPORTANT RULES:
- Separate required skills from nice-to-have skills carefully
- Only include skills explicitly mentioned in the posting
- Extract minimum experience requirements accurately
- Do not add requirements that aren't in the posting
- If no minimum experience is stated, write "Not specified"

Job Description:
{jd_text}

{format_instructions}
"""

EVALUATION_PROMPT = """You are an expert technical recruiter evaluating a candidate's fit for a role.

Compare the candidate's skills against the job requirements and provide a fair, detailed evaluation.

SCORING RULES:
- Score 0-100 based on skill match percentage
- Required skills carry more weight than nice-to-have skills
- Consider years of experience alignment
- Be specific about which skills match and which are missing
- Don't penalize for having extra skills not in the requirements
- A score of 80+ means strong match, 60-79 is moderate, 40-59 is partial, below 40 is weak

Candidate Skills:
{resume_skills}

Job Requirements:
{job_requirements}

{format_instructions}
"""
