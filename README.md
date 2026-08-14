# Resume Screener

AI-powered resume screening tool that uses a LangChain LCEL pipeline to extract skills from resumes, compare against job descriptions, and provide scored rankings with detailed reasoning.

## Features

- Upload PDF, DOCX, or TXT resumes
- AI-powered skill extraction and matching
- 0-100 scoring with detailed reasoning
- Ranked candidate results
- React web UI with 3D glassmorphism design + REST API (FastAPI) + CLI

## Tech Stack

- **AI Pipeline**: LangChain (LCEL) + Pydantic for structured LLM output
- **LLM**: OpenRouter (GPT-4o-mini / Claude 3.5 Sonnet)
- **Backend**: FastAPI (in-memory storage)
- **Frontend**: React + Vite (3D glassmorphism dark-mode UI)
- **File Parsing**: PyMuPDF (PDF) + python-docx (DOCX)
- **Tracing**: LangSmith (optional)

## Setup

### 1. Clone & Install Backend

```bash
git clone <repo-url>
cd resume-screener
pip install -r requirements.txt
```

### 2. Install Frontend

```bash
cd frontend
npm install
```

### 3. Configure API Keys

Edit `.env` and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_key_here
```

Get one at https://openrouter.ai/keys

### 4. Generate Sample Data (Optional)

```bash
python setup_data.py
```

## Usage

### Web App

Start the API server and React dev server in two terminals:

```bash
# Terminal 1: FastAPI backend
uvicorn app.api:app --reload --port 8000
```

'''

# Terminal 2: React frontend

cd frontend
npm run dev
'''
Open http://localhost:5173 in your browser.

### CLI

```bash
python main.py --resume data/resumes/sample_resume.txt --jd data/job_description.txt
```

### API Only

```bash
uvicorn app.api:app --reload --port 8000
```

API docs at http://localhost:8000/docs

## Project Structure

```
resume-screener/
├── app/
│   ├── api.py          # FastAPI routes (in-memory storage)
│   └── schemas.py      # API request/response models
├── chains/
│   ├── models.py       # Pydantic output schemas
│   └── pipeline.py     # LCEL extraction + scoring pipeline
├── frontend/           # React + Vite app
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── components/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── data/
│   ├── resumes/        # Sample resumes for testing
│   └── job_description.txt
├── parsers/
│   └── file_parser.py  # PDF/DOCX/TXT text extraction
├── prompts/
│   └── templates.py    # Anti-hallucination prompt templates
├── main.py             # CLI entrypoint
├── setup_data.py       # Sample data generator
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
└── README.md
```

## API Endpoints

| Method | Route                  | Purpose                |
| ------ | ---------------------- | ---------------------- |
| POST   | /api/jobs              | Create a job posting   |
| POST   | /api/jobs/{id}/resumes | Upload & score resumes |
| GET    | /api/jobs/{id}/results | Get ranked results     |
| GET    | /api/candidates/{id}   | Candidate detail       |
| GET    | /api/jobs              | List all jobs          |
