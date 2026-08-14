import argparse
import os
import sys
from dotenv import load_dotenv

from parsers.file_parser import parse_file


def parse_args():
    parser = argparse.ArgumentParser(
        description="AI-powered Resume Screener CLI - screen and score resumes against job descriptions."
    )
    parser.add_argument(
        "--resume",
        type=str,
        required=True,
        help="Path to the candidate resume file (supported formats: .pdf, .docx, .txt)",
    )
    parser.add_argument(
        "--jd",
        type=str,
        required=True,
        help="Path to the job description file (supported formats: .pdf, .docx, .txt)",
    )
    return parser.parse_args()


def check_api_key():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key or api_key.strip() == "" or api_key == "your_openrouter_api_key_here":
        print(
            "Error: OPENROUTER_API_KEY is not configured or is set to placeholder.\n"
            "Please set your OpenRouter API key in the .env file or as an environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)


def get_field_value(obj, field_name, default=None):
    if isinstance(obj, dict):
        return obj.get(field_name, default)
    return getattr(obj, field_name, default)


def print_screening_results(result):
    score = get_field_value(result, "score", 0)
    matched_skills = get_field_value(result, "matched_skills", [])
    missing_skills = get_field_value(result, "missing_skills", [])
    reasoning = get_field_value(result, "reasoning", "No reasoning provided.")

    print("\n" + "=" * 60)
    print("                 RESUME SCREENING RESULTS")
    print("=" * 60)
    print(f"Score: {score}/100\n")

    print("Matched Skills:")
    if matched_skills:
        for skill in matched_skills:
            print(f"  - {skill}")
    else:
        print("  - None")

    print("\nMissing Skills:")
    if missing_skills:
        for skill in missing_skills:
            print(f"  - {skill}")
    else:
        print("  - None")

    print("\nReasoning:")
    print(f"{reasoning}")
    print("=" * 60 + "\n")


def main():
    load_dotenv()
    args = parse_args()

    # Verify files exist
    if not os.path.exists(args.resume):
        print(f"Error: Resume file not found at '{args.resume}'", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.jd):
        print(f"Error: Job description file not found at '{args.jd}'", file=sys.stderr)
        sys.exit(1)

    # Verify API key
    check_api_key()

    # Parse resume file
    try:
        resume_text = parse_file(args.resume)
    except Exception as e:
        print(f"Error parsing resume file '{args.resume}': {e}", file=sys.stderr)
        sys.exit(1)

    # Parse job description file
    try:
        jd_text = parse_file(args.jd)
    except Exception as e:
        print(f"Error parsing job description file '{args.jd}': {e}", file=sys.stderr)
        sys.exit(1)

    # Run screening pipeline
    try:
        from chains.pipeline import run_pipeline

        print("Analyzing resume against job description...")
        result = run_pipeline(resume_text, jd_text)
        print_screening_results(result)
    except ImportError as e:
        print(
            f"Error importing screening pipeline: {e}\n"
            "Ensure chains/pipeline.py is available.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"Error during screening pipeline execution: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
