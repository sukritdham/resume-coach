from datetime import datetime
import os
import json

def log_resume_case(resume_text, job_description, coach_output, log_file="resume_cases.json"):
    """
    Save inputs + outputs to a JSON file.Appends to a list in JSON.
    This file can be used for evaluation purposes.
    :param resume_text:
    :param job_description:
    :param coach_output:
    :param log_file:
    :return:
    """
    case = {
        "timestamp": datetime.utcnow().isoformat(),
        "resume": resume_text,
        "job_description": job_description,
        "resume_coach_output": coach_output,
    }

    # If file exists, load it, otherwise start a new list
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append the new case
    data.append(case)

    # Write back to JSON
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)