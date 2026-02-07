from models.call_llm import call_llm
from common.context import context_store
from models.prompts import RESUME_CHAT_LOOP
from processing.cleaner import clean_and_parse_output

# Bot response in the event the LLM returns an empty response
fallback = (
    "I couldn’t generate a complete response this time. Please try rephrasing your question."
)

# Bot response handler to manage responses to maintain consistent UX
def botreply_handler(parsed, fallback_text):
    botreply = parsed.get("botreply")

    if not isinstance(botreply, str):
        return fallback_text

    if not botreply.strip():
        return fallback_text

    return botreply

# --- Chatbot handler ---
def chat_loop(user_message, history, provider, model):
    """
    Chatbot handler that recieves user input, constructs the prompt for purposes of model invocation
    and invokes model call wrapper.
    :param user_message: user input into chatbot
    :param history: past history from user
    :param provider: LLM provider (Replicate|OpenAI)
    :param model: Model Name
    :return: formatted model response
    """
    resume_text = context_store["resume_text"]
    job_description = context_store["job_description"]
    classification = context_store["classification"]
    assessment = context_store["assessment"]
    rewrite_output = context_store["rewritten_text"]
    suggestion_output = context_store["suggestion"]

    # System prompt
    system_prompt = (RESUME_CHAT_LOOP
    + f"Resume:{resume_text} Job Description:{job_description}"
      f"Classification:{classification} Assessment:{assessment} Rewritten text if 'YES OR MAYBE': {rewrite_output}"
      f"Suggestion if 'NO':{suggestion_output}".strip())

    formatted_messages = [{"role": "system", "content": system_prompt}]

    if history:
        for user_msg, bot_msg in history:
            formatted_messages.append({"role": "user", "content": str(user_msg)})
            formatted_messages.append({"role": "assistant", "content": str(bot_msg)})

    # Add the new message from the user
    formatted_messages.append({"role": "user", "content": str(user_message)})

    # Call LLM
    bot_reply = call_llm(provider, model, formatted_messages)
    # Parse output JSON
    output = clean_and_parse_output(bot_reply)
    # Update Gradio history (Gradio wants tuples)
    history = history or []
    history.append((user_message, botreply_handler(output, fallback)))

    return history, history