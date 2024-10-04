import gradio as gr
from huggingface_hub import InferenceClient
import torch
from transformers import pipeline
import os
# import google.generativeai as genai

# Global flag to handle cancellation
stop_inference = False


def load_model(input_text, use_local, selected_language):
    pass

# Create the Gradio interface
def create_gradio_interface():
    with gr.Blocks() as demo:
        # Center-align the header
        gr.Markdown("<h1 style='text-align: center;'>MultiLingo AI</h1>")  # Center-aligned h1 header
        gr.Markdown("<p style='text-align: center;'>Ask a question and get a response in any language you desire</p>")

        # Layout for input/output textboxes side by side
        with gr.Row():
            user_input = gr.Textbox(label="Enter your query here", lines=10)  # Square-like input box
            chatbot_output = gr.Textbox(label="AI Response", lines=10)  # Square-like output box

        # Checkbox for selecting local or API-based model
        use_local = gr.Checkbox(label="Use local model", interactive=True)

        # Dropdown for language selection
        languages = ["English", "Hindi", "Spanish", "French", "German"]  # Add more languages as needed
        language_selector = gr.Dropdown(label="Select response language", choices=languages, value="English")

        # Button to trigger the response
        submit_button = gr.Button("Submit")

        # Button functionality
        submit_button.click(
            load_model,
            inputs=[user_input, use_local, language_selector],
            outputs=chatbot_output
        )

    return demo


if __name__ == "__main__":
    demo = create_gradio_interface()
    demo.launch(share=False)