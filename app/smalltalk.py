import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq()

def talk(query):
    prompt = f"""
You are a friendly and conversational assistant for an e-commerce website.

Respond casually and naturally to the user's message.

User: {query}
"""

    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=os.environ['GROQ_MODEL'],
    )

    return chat_completion.choices[0].message.content


# testing
if __name__ == "__main__":
    query = "How are you?"
    response = talk(query)
    print(response)