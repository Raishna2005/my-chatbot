import os
import gradio as gr
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Load the secret variables from the .env file
load_dotenv()
my_secret_token = os.getenv("HUGGINGFACE_TOKEN")

# 2. Use the variable in your client
client = InferenceClient("Qwen/Qwen2.5-7B-Instruct", token=my_secret_token)

def chat_function(message, history):
    response = ""
    for message_chunk in client.chat_completion(
        messages=[{"role": "user", "content": message}],
        max_tokens=500,
        stream=True,
    ):
        token = message_chunk.choices[0].delta.content
        if token:
            response += token
            yield response

demo = gr.ChatInterface(fn=chat_function, title="Secure AI Chatbot")

if __name__ == "__main__":
    demo.launch()