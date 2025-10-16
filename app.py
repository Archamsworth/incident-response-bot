import os
import gradio as gr
from llama_cpp import Llama

# Load your model
llm = Llama(model_path="model.bin")  # model.bin must be in the repo

def chatbot(user_input):
    response = llm(user_input)
    return response

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Describe the incident..."),
    outputs=gr.Textbox(label="Response"),
    title="Incident Response Chatbot",
    description="AI assistant for guiding security incident response steps"
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    iface.launch(server_name="0.0.0.0", server_port=port)
