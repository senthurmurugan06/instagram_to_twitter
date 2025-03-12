import openai
import os
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def summarize_text(text):
    prompt = f"Summarize the following Instagram post into a tweet (max 280 chars):\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    return response["choices"][0]["message"]["content"].strip()
