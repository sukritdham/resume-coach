from common.config import replicate_client
from utils.logger_config import logging

def call_replicate_model(prompt, model_name):
    """
    replicate model call wrapper
    :param prompt: prompt to model
    :param model_name: model name
    :return: model response
    """
    logging.debug(f"replicate prompt:{prompt}")
    logging.info(f"REPLICATE")
    output = replicate_client.run(
        model_name,
        input={"prompt": prompt, "temperature": 0.7, "max_new_tokens": 500}
    )
    return "".join(output)