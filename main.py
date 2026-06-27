import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def run():
    prompt = """
You are an assistant that finds international art open calls.

Return 5 real-looking opportunities:
Name / Country / Type / Deadline / Why relevant

Focus on funding and no long residency.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    data = response.json()

    # 🧠 关键：防止结构为空直接崩
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        print("Gemini API returned unexpected response:")
        print(data)
        raise Exception("Gemini response invalid or blocked")

    with open("output.md", "w") as f:
        f.write(text)

    print(text)

run()
