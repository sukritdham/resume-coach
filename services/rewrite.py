from models.openai_client import call_openai_model
from models.replicate_client import call_replicate_model
from processing.cleaner import clean_and_parse_output
from models.prompts import RESUME_REWRITE_PROMPT
from utils.logger_config import logging

def rewrite_resume(resume_text, job_desc, model_type, model_name, assessment):
    prompt = RESUME_REWRITE_PROMPT + f"Resume:{resume_text} Job Description:{job_desc} Assessment Summary:{assessment}"

    try:
        if model_type == "Replicate":
            logging.info(f"rewrite resume REPLICATE")
            raw_output = call_replicate_model(prompt, model_name)
            output = clean_and_parse_output(raw_output)
            logging.debug(f"REWRITE_OUTPUT:{output}")
            return output["rewritten_resume_text"]

        elif model_type == "OpenAI":
            raw_output = call_openai_model(prompt, model_name)
            output = clean_and_parse_output(raw_output)
            logging.debug(f"REWRITE_OUTPUT:{output}")
            return output["rewritten_resume_text"]

        else:
            return f"Unsupported model: {model_type}"

    except Exception as e:
        return f"Error during model call: {str(e)}"
