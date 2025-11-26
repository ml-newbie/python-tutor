# tutor_bot.py
import os
from openai import OpenAI

# Load API key
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found.")

# Initialize client
client = OpenAI(api_key=api_key)

def ask_python_tutor(question: str, chat_history: list[dict] = None) -> str:
    """
    Ask the GPT model a Python question.
    chat_history: list of {"role": "user"/"assistant", "content": "..."} for context
    """
    if chat_history is None:
        chat_history = []

    # Prepend system instruction
    messages = [{"role": "system", "content": "You are a helpful Python coding tutor. Explain concepts clearly and provide example code when appropriate."}]
    messages += chat_history
    messages.append({"role": "user", "content": question})

    # Use the new client API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=messages,
        temperature=0.3,
        max_tokens=500
    )

    answer = response.choices[0].message.content.strip()
    return answer
