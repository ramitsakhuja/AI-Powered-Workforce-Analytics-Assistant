import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def explain_answer(question, sql_answer):
    """
    Converts SQL output into a professional business explanation.
    """

    prompt = f"""
You are an HR Analytics Assistant.

A SQL query has already calculated the correct answer.

Do NOT change the numbers.

Simply explain the answer in simple business language.

User Question:
{question}

SQL Result:
{sql_answer}

Rules:
- Keep the response under 80 words.
- Use professional HR/business language.
- Do not invent facts.
- Use only the SQL result provided.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content