import gradio as gr
from services.assessment import assess_resume
from chatbot.chat_loop import chat_loop
from utils.logger_config import logging

logging.debug("STARTING RESUME COACH")

def update_provider_default_model(provider):
    if provider == "OpenAI":
        return "gpt-4o"
    elif provider == "Replicate":
        return "google/gemini-2.5-flash"
    else:
        return ""

OPENAI_MODELS = ["gpt-4o", "gpt-5.1", "gpt-5.2"]
REPLICATE_MODELS = ["google/gemini-2.5-flash", "deepseek-ai/deepseek-r1", "anthropic/claude-4-sonnet"]

def update_model_names(selected_type):
    if selected_type == "OpenAI":
        return gr.update(choices=OPENAI_MODELS, value=OPENAI_MODELS[0])
    return gr.update(choices=REPLICATE_MODELS, value=REPLICATE_MODELS[0])

with gr.Blocks() as demo:
    gr.Markdown("## Resume Coach with Chatbot")

    # TAB 1 — Resume Assessment
    with gr.Tab("Resume Assessment"):
        with gr.Row():
            with gr.Column():
                resume_input = gr.File(label="Upload Resume (PDF)", file_types=[".pdf"])

            with gr.Column():
                job_input = gr.Textbox(
                    label="Paste Job Description",
                    lines=10,
                    placeholder="Job description here..."
                )

        model_type = gr.Dropdown(
            ["OpenAI", "Replicate"],
            label="Model Type",
            value="OpenAI"
        )

        model_name = gr.Dropdown(
            OPENAI_MODELS,
            label="Model Name"
        )

        model_type.change(
            fn=update_model_names,
            inputs=model_type,
            outputs=model_name
        )

        with gr.Row():
            classification = gr.Label(label="Classification (YES / MAYBE / NO)")
            assessment = gr.Textbox(label="Assessment", lines=12)
            submit_btn = gr.Button("Get Assessment")

        with gr.Row():
            rewritten_resume = gr.Textbox(label="Rewritten Resume (if YES/MAYBE)", lines=10)
            suggestions = gr.Textbox(label="Suggestions (if NO)", lines=10)

        # Hook up main assessment call
        submit_btn.click(
            fn=assess_resume,
            inputs=[resume_input, job_input, model_type, model_name],
            outputs=[classification, assessment, rewritten_resume, suggestions]
        )

    # TAB 2 — Chat with Resume Coach
    with gr.Tab("Chat with Resume Coach"):
        with gr.Row():
            state = gr.State([])
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Your Message")
            clear = gr.Button("Clear Chat")

            # Button triggers chat loop
            msg.submit(
                fn=chat_loop,
                inputs=[msg, state, model_type, model_name],
                outputs=[chatbot, state]
            )
            # Clear chat window
            clear.click(
                fn=lambda: ([], []),
                inputs=None,
                outputs=[chatbot, state]
            )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
