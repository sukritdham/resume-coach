from processing.reader import extract_text_from_pdf
from processing.cleaner import clean_and_parse_output
from common.context import context_store
from models.openai_client import call_openai_model
from models.replicate_client import call_replicate_model
from models.prompts import RESUME_ASSESSMENT_PROMPT
from utils.store import log_resume_case
from .suggest import suggestion
from .rewrite import rewrite_resume
from utils.logger_config import logging

def assess_resume(resume_file, job_desc, model_type, model_name):
    if resume_file is None or job_desc.strip() == "":
        return "Please upload a resume and paste a job description."

    # Extract resume text
    resume_text = extract_text_from_pdf(
        resume_file.name)  # this function only handles pdf, need to handle additional types
    rewrite_output = ""
    suggestion_output = ""
    output = {}
    output["classification"] = ""
    output["assessment"] = ""

    prompt = RESUME_ASSESSMENT_PROMPT + f"Resume:{resume_text} Job Description:{job_desc}"

    try:
        if model_type == "Replicate":
            logging.info(f"assess resume REPLICATE")
            raw_output = call_replicate_model(prompt, model_name)
            logging.debug(f"RAW_OUTPUT:{raw_output}")
            output = clean_and_parse_output(raw_output)
            if output["classification"] == "YES" or output["classification"] == "MAYBE":
                rewrite_output = rewrite_resume(resume_text, job_desc, model_type, model_name, output["assessment"])
                logging.debug(f"rewrite_output:{rewrite_output}")
            else:
                suggestion_output = suggestion(resume_text, job_desc, model_type, model_name, output["assessment"])
                logging.debug(f"suggestion:{suggestion_output}")
            log_resume_case(resume_text, job_desc, output)
            return output["classification"], output["assessment"], rewrite_output, suggestion_output

        elif model_type == "OpenAI":
            raw_output = call_openai_model(prompt, model_name)
            logging.debug(f"RAW_OUTPUT:{raw_output}")
            output = clean_and_parse_output(raw_output)
            if output["classification"] == "YES" or output["classification"] == "MAYBE":
                rewrite_output = rewrite_resume(resume_text, job_desc, model_type, model_name, output["assessment"])
                logging.debug(f"rewrite_output:{rewrite_output}")
            else:
                suggestion_output = suggestion(resume_text, job_desc, model_type, model_name, output["assessment"])
                logging.debug(f"suggestion:{suggestion_output}")
            log_resume_case(resume_text, job_desc, output)
            return output["classification"], output["assessment"], rewrite_output, suggestion_output

        else:
            return f"Unsupported model: {model_type}"

    except Exception as e:
        return f"Error during model call: {str(e)}"

    finally:
        context_store["resume_text"] = resume_text
        context_store["job_description"] = job_desc
        context_store["classification"] = output["classification"]
        context_store["assessment"] = output["assessment"]
        context_store["rewritten_text"] = rewrite_output
        context_store["suggestion"] = suggestion_output