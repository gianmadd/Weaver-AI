import os
from typing import Optional

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Configure the API key
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)
model = "llama-3.1-70b-versatile"


def send_prompt(prompt: str) -> str:
    """
    Sends the prompt to the Groq model and handles the response.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt},
            ],
            model=model,
            temperature=0.6,
            top_p=0.8,
            frequency_penalty=0.5,
            presence_penalty=0.1,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during story generation: {str(e)}"
