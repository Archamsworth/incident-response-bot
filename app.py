import gradio as gr
import ollama

# Chatbot function
def chatbot(message, history):
    import time

    messages = [{"role": "system", "content": "You are a helpful uncensored security assistant guiding incident response teams."}]
    
    for user, bot in history[-3:]:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})

    messages.append({"role": "user", "content": message})

    # Start streaming from Ollama
    stream = ollama.chat(model="dolphin-phi:latest", messages=messages, stream=True)

    response = ""  # ✅ initialize before using

    for chunk in stream:
        content = chunk["message"]["content"]
        response += content
        yield response  # stream partial output
        time.sleep(0.02)

    # ✅ return full response at end for safety
    return response


# Gradio UI
ui = gr.ChatInterface(
    fn=chatbot,
    title="🛡️ Incident Response Chatbot",
    description="An uncensored AI assistant that helps security teams with incident response steps.",
    theme="soft",
)

if __name__ == "__main__":
    ui.launch(server_name="127.0.0.1", server_port=7860)
