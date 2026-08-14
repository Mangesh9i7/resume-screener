import os

def bootstrap_sample_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    resumes_dir = os.path.join(data_dir, "resumes")

    os.makedirs(resumes_dir, exist_ok=True)

    sample_resume_content = """Alex Rivera
Senior Software Engineer
Email: alex.rivera@example.com | Phone: (555) 234-5678 | GitHub: github.com/alexrivera | LinkedIn: linkedin.com/in/alexrivera-dev
Location: San Francisco, CA

PROFESSIONAL SUMMARY
Results-driven Full-Stack Software Engineer with 5+ years of experience building high-performance web applications, distributed backend services, and scalable cloud architectures. Proficient in Python, TypeScript, React, FastAPI, and Docker. Strong background in database design, RESTful API architecture, and CI/CD automation.

TECHNICAL SKILLS
- Programming Languages: Python, TypeScript, JavaScript, SQL, HTML5, CSS3
- Backend Frameworks & Libraries: FastAPI, Flask, Django, Node.js, Express, Pydantic, SQLAlchemy
- Frontend Frameworks: React, Next.js, Redux Toolkit, Tailwind CSS
- Databases & Storage: PostgreSQL, MySQL, Redis, MongoDB
- DevOps & Cloud: Docker, Kubernetes, AWS (EC2, S3, RDS, Lambda), GitHub Actions, CI/CD
- Tools & Practices: Git, Agile/Scrum, REST APIs, Microservices, Test-Driven Development (pytest, Jest)

PROFESSIONAL EXPERIENCE

Senior Software Engineer | ApexCloud Solutions, San Francisco, CA
June 2021 – Present
- Designed and built scalable RESTful microservices in Python (FastAPI) and PostgreSQL, handling over 10M requests daily with 99.95% uptime.
- Developed interactive web dashboards with React and TypeScript, improving user engagement by 35%.
- Implemented distributed caching strategies using Redis, reducing API response times by 45%.
- Containerized applications using Docker and deployed workloads onto AWS infrastructure using automated GitHub Actions CI/CD pipelines.
- Mentored junior engineers, led code reviews, and championed best practices in unit and integration testing with pytest.

Software Engineer | DevPulse Technologies, Austin, TX
July 2019 – May 2021
- Developed backend API endpoints using Python (Django/Flask) and integrated with third-party payment and messaging services.
- Created responsive frontend components using React and Redux for customer-facing web applications.
- Optimized complex SQL queries and database schemas in PostgreSQL, cutting query execution times by 30%.
- Participated in sprint planning, agile grooming, and daily stand-ups within a cross-functional engineering team.

EDUCATION
Bachelor of Science in Computer Science
University of California, Berkeley | 2015 – 2019

PROJECTS
- AI Document Summarizer: Built a web tool using FastAPI, LangChain, and React to extract insights and generate summaries from large PDF documents.
- Real-Time Task Tracker: Full-stack collaboration application featuring real-time updates via WebSockets, built with TypeScript, Node.js, and Redis.
"""

    job_description_content = """Job Title: Senior Full-Stack Engineer
Company: CloudScale Innovations
Location: Remote (US) / San Francisco, CA
Employment Type: Full-Time

About the Role:
We are looking for an experienced and passionate Senior Full-Stack Engineer to lead the design and development of our next-generation cloud analytics platform. You will collaborate with product designers, data engineers, and fellow software engineers to deliver robust, high-impact features from database to browser.

Key Responsibilities:
- Design, build, and maintain efficient, reusable, and reliable backend services and APIs using Python (FastAPI/Django).
- Architect and develop modern, responsive user interfaces using React and TypeScript.
- Design relational database schemas and optimize query performance with PostgreSQL and Redis caching.
- Build and maintain CI/CD pipelines and containerized deployments using Docker and cloud infrastructure (AWS/GCP).
- Write comprehensive unit, integration, and end-to-end tests to ensure software reliability.
- Collaborate with product managers and cross-functional teams to define technical requirements and architecture.

Required Qualifications:
- 4+ years of professional full-stack software development experience.
- Strong proficiency in Python with frameworks such as FastAPI, Flask, or Django.
- Solid experience with modern frontend development using React, TypeScript, and modern state management.
- Strong database knowledge with PostgreSQL, SQL optimization, and data modeling.
- Experience with containerization using Docker and automated CI/CD workflows (e.g., GitHub Actions).
- Proven track record of designing, building, and deploying RESTful APIs and microservices.
- Experience with cloud platforms such as AWS or Google Cloud Platform.

Preferred Qualifications:
- Experience with LangChain, OpenAI APIs, or LLM-powered application development.
- Familiarity with Kubernetes and container orchestration.
- Knowledge of GraphQL APIs and WebSocket streaming.
- Strong understanding of web security best practices (OAuth2, JWT, CORS, HTTPS).
"""

    sample_resume_path = os.path.join(resumes_dir, "sample_resume.txt")
    job_description_path = os.path.join(data_dir, "job_description.txt")

    with open(sample_resume_path, "w", encoding="utf-8") as f:
        f.write(sample_resume_content)

    with open(job_description_path, "w", encoding="utf-8") as f:
        f.write(job_description_content)

    print(f"Sample data created successfully!")
    print(f"  - Resume file: {sample_resume_path}")
    print(f"  - Job Description: {job_description_path}")

if __name__ == "__main__":
    bootstrap_sample_data()
