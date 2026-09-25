# google-generativeai, os
import os
import google.generativeai as genai # Official Gemini API SDK
from dotenv import load_dotenv 
load_dotenv()


# genai.configure(api_key=api_key)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #getpass.getpass() -> os.getenv("GOOGLE_API_KEY"): api_key variable

#GOOGLE_API_KEY="paste the copied api key from the dashboard" - > .env


def chat_with_gemini(user_input):
    model = genai.GenerativeModel('gemini-3.6-flash')  # Or 'gemini-1.5-flash' for free tier Instantiating the model that i will use?

    #PICIO -> Input
    # Prepare the prompt
    prompt = f"""You are a Data science instructor. Help the user with the query User: {user_input}
    Bot:"""
    print(f"Promt is: {prompt}")
    # Generate the response
    response = model.generate_content([prompt])

    # Clean the response using the to_markdown function
    cleaned_response = response.text

    return cleaned_response

def run_chatbot():
    print("Welcome to the Gemini Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chat ended.")
            break
        response = chat_with_gemini(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_chatbot()# Run the chatbot
