import openai
import os
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text():
    # كلمات مفتاحية لبداية الجملة
    keywords = [
        "Did you know that",
        "Here's a shocking fact:",
        "Let's talk about this:",
        "Unbelievable but true:",
        "Get this:",
        "Surprisingly,"
    ]

    intro = random.choice(keywords)

    # أرسل الطلب لـ GPT مع الكلمات المفتاحية
    prompt = f"{intro} give me a short, interesting fact in one sentence for a short vertical video."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"].strip()
