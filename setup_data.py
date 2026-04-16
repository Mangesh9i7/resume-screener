import os

os.makedirs("data/resumes", exist_ok=True)

job_description = """
Role: Software Engineer
Requirements:
- 2+ years of experience in software development.
- Strong proficiency in Python and JavaScript.
- Experience with web frameworks like Django or React.
- Knowledge of SQL and database design.
- Good problem-solving and teamwork skills.
"""

resumes = {
    "strong": "Software Engineer with 3 years of experience. Skilled in Python, JavaScript, Django, and React. Designed scalable web applications and optimized SQL databases. Strong collaborator with excellent communication skills.",
    "average": "Junior Developer with 1.5 years of experience. Comfortable with Python and JavaScript. Built small projects using Flask and basic SQL. Eager to learn more about React and Django.",
    "weak": "Recent graduate with a degree in History. Limited programming experience, mostly in HTML and CSS. No professional software development background yet, but motivated to learn."
}

with open("data/job_description.txt", "w") as f:
    f.write(job_description)

for name, content in resumes.items():
    with open(f"data/resumes/{name}.txt", "w") as f:
        f.write(content)

print("Data files created successfully in the 'data/' folder!")