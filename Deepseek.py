import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenRouter API key
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("Error: OPENROUTER_API_KEY environment variable not set.")
    print("Please set it in a .env file or export it in your terminal.")
    exit(1)

#  DeepSeek model
MODEL = "deepseek/deepseek-r1-0528:free"

# System message to specialize it in Computer Science
chat_history = [
    {
        "role": "system",
        "content": (
            "You are a Computer Science tutor. You explain topics like OS, DBMS, Networking, Algorithms, AI, "
            "Data Structures, etc. Use simple language, give examples, and explain like a teacher."
        )
    }
]

print(" DeepSeek CS Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print(" Chat ended.")
        break

    # Add user's message to history
    chat_history.append({"role": "user", "content": user_input})

    #  Set headers required by OpenRouter
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost", 
        "X-Title": "DeepSeekCSBot"           
    }

    #  Construct request body
    data = {
        "model": MODEL,
        "messages": chat_history
    }

    # Send request to OpenRouter API
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        print("AI:", reply.strip())
        # Add AI's message to chat history
        chat_history.append({"role": "assistant", "content": reply})
    else:
        print("Error:", response.status_code)
        print(response.text)
        break
