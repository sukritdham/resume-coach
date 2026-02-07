from models.openai_client import call_openai_model
from models.replicate_client import call_replicate_model
from processing.cleaner import clean_and_parse_output
from models.prompts import RESUME_SUGGESTION_PROMPT
from utils.logger_config import logging

def suggestion(resume_text, job_desc, model_type, model_name, assessment):
    prompt = RESUME_SUGGESTION_PROMPT + f"Resume:{resume_text} Job Description:{job_desc} Assessment Summary:{assessment}"

    try:
        if model_type == "Replicate":
            logging.info(f"suggestion REPLICATE")
            raw_output = call_replicate_model(prompt, model_name)
            output = clean_and_parse_output(raw_output)
            logging.debug(f"SUGGESTION:{output}")
            return output["suggestion"]

        elif model_type == "OpenAI":
            raw_output = call_openai_model(prompt, model_name)
            output = clean_and_parse_output(raw_output)
            logging.debug(f"SUGGESTION:{output}")
            return output["suggestion"]

        else:
            return f"Unsupported model: {model_type}"

    except Exception as e:
        return f"Error during model call: {str(e)}"