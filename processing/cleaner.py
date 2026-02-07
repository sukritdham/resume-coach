import json
import re

def clean_and_parse_output(raw_output: str):
    """
    Defensive parser to parse & clean the LLM output
    :param raw_output: raw output
    :return: cleaned and parsed output
    """
    try:
        text = raw_output.strip()

        # Sanity check
        if not text:
            return {
                "status": "empty_response",
                "user_message": (
                    "I didn’t receive a response this time. "
                    "Please try again or rephrase your request."
                )
            }

        # Extract JSON inside ```json ... ```
        fenced = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
        if fenced:
            return json.loads(fenced.group(1))

        # Extract the first block
        block = re.search(r"\{.*?\}", text, re.DOTALL)
        if block:
            return json.loads(block.group(0))

        # Try parsing raw output only if it looks like JSON
        if text.startswith("{") and text.endswith("}"):
            return json.loads(text)

        raise ValueError("No JSON object found")

    except Exception as e:
        # raise ValueError(f"Failed to extract JSON: {e}\nRAW OUTPUT:\n{raw_output}")
        # Fallback: wrap text into JSON
        return {
            "status": "unstructured_response",
            "user_message": (
                "I analyzed your input, but couldn’t format the results cleanly. "
                "Here’s a readable summary instead."
            ),
            "summary": text
        }