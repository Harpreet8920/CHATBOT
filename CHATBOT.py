import os
import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-hABrbMJju4BL8Vml9oN9T3BlbkFJsssNpT07jrrDDzPPYDRM"


# Function to interact with GPT-3.5 model
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()


# Main function to run the chatbot
def main():
    print("Welcome to the Chatbot!")
    print(
        "You can start chatting. Type 'quit', 'exit', or 'bye' to end the conversation."
    )

    # Chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
