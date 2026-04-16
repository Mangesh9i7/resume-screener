import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from prompts.templates import extraction_prompt, evaluation_prompt
from chains.models import ExtractedInfo, EvaluationResult

# 1. Load the environment variables
load_dotenv()

# 2. Grab the key (Hardcode it right here just for this test!)
my_key = os.getenv("OPENROUTER_API_KEY")

# 3. Bulletproof OpenRouter initialization
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=my_key,

    model="openai/gpt-4o-mini", 
    temperature=0,
    model_kwargs={
        "extra_headers": {
            "Authorization": f"Bearer {my_key}",
            "HTTP-Referer": "https://github.com/Vishwajit", 
            "X-Title": "Resume Screener"
        }
    }
)

# 4. Create the Extraction Step
extraction_step = extraction_prompt | llm.with_structured_output(ExtractedInfo)

# 5. Create the Evaluation Step
evaluation_step = evaluation_prompt | llm.with_structured_output(EvaluationResult)

# 6. Build the Full LCEL Pipeline (THIS IS WHAT WAS MISSING!)
pipeline = (
    RunnablePassthrough.assign(extracted_details=extraction_step)
    | evaluation_step
)