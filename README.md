# DeepSeek CS Chatbot

A simple command-line chatbot acting as a Computer Science tutor. This bot uses the DeepSeek model via the OpenRouter API to explain topics like OS, DBMS, Networking, Algorithms, AI, Data Structures, etc.

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Install the required libraries:
   ```bash
   pip install requests python-dotenv
   ```

2. Create a `.env` file in the same directory as the script and add your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY="your_api_key_here"
   ```

## Usage

Run the script from your terminal:

```bash
python Deepseek.py
```

Type your questions or topics you want to learn about, and the bot will reply with explanations. Type `exit` or `quit` to end the chat.

## Example

```
 DeepSeek CS Chatbot (type 'exit' to quit)

You: Explain how a hash table works.
AI: A hash table is a data structure that stores key-value pairs...
```
