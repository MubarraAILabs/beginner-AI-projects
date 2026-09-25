import gradio as gr
from simple_chat import chat_with_gemini


# Create a Gradio interface
def chatbot_interface(user_input):
    return chat_with_gemini(user_input)

# Set up the Gradio interface
iface = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text", title="Gemini Chatbot",
                     description="Chatbot powered by Gemini 3.6 flash. Ask me anything!")
iface.launch(share=True) #share=True