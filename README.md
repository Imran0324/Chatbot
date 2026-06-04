# CS Chatbot

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

## Changing the Model

By default, this chatbot uses a DeepSeek model. However, since it connects via the OpenRouter API, you can easily switch to **any other model** supported by OpenRouter (such as OpenAI's GPT-4o, Anthropic's Claude, Meta's Llama 3, etc.).

To change the model:
1. Open the python script (e.g., `Deepseek.py` or `chatbot.py`).
2. Locate the `MODEL` variable near the top of the file:
   ```python
   MODEL = "deepseek/deepseek-r1-0528:free"
   ```
3. Change its value to the ID of any model you prefer from the [OpenRouter Models page](https://openrouter.ai/models). For example:
   ```python
   MODEL = "openai/gpt-4o"
   ```

## Example

```
 DeepSeek CS Chatbot (type 'exit' to quit)

You: Explain how a hash table works.
AI: A hash table is a data structure that stores key-value pairs...
```
