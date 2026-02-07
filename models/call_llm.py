from common.config import openai_client,replicate_client
from utils.logger_config import logging

# --- Unified LLM call for ChatBOT ---
def call_llm(provider, model, messages):
    """
    Call LLM
    :param provider: LLM provider (Replicate|OpenAI)
    :param model: model name
    :param messages: prompt to model
    :return: model response
    """
    logging.debug(f"LLM messages = {messages}")

    if provider == "OpenAI":
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    elif provider == "Replicate":
        logging.info(f"call llm REPLICATE")
        # Flatten messages into one long prompt
        combined = "\n".join(
            f"{m['role']}: {m['content']}" for m in messages
        )

        response = replicate_client.run(model, input={"prompt": combined})

        if isinstance(response, (list, tuple)):
            response = "".join(response)
        return str(response).strip()

    else:
        return "Unsupported provider"

