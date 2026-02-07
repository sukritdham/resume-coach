from common.config import openai_client
from utils.logger_config import logging

def call_openai_model(prompt, model):
    """
    openai model call wrapper
    :param prompt: prompt to model
    :param model: model name
    :return: model response
    """
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content