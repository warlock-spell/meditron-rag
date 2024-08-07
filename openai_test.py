# chat_completion_example.py

import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

from openai import OpenAI

client = OpenAI(
    api_key=openai_api_key,
    base_url="https://api.aimlapi.com",
)

print(client)

response = client.chat.completions.create(
    # model="mistralai/Mistral-7B-Instruct-v0.2",
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {"role": "user", "content": "Tell me, why is the sky blue?"},
    ],
)

message = response.choices[0].message.content
print(f"Assistant: {message}")
