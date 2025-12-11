import os
from openai import OpenAI

# Read key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
