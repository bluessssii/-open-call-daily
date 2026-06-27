import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def run():
    prompt = """
You are an assistant that finds international art open calls.

Rules:
- Prefer funding / grants / cash awards
- Avoid long residency requirements
- Japan and France allowed if funded
- Avoid application fees if possible

Return 5 structured opportunities:
Name / Country / Type / Deadline / Why relevant
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
    result = response.json()

    text = result["candidates"][0]["content"]["parts"][0]["text"]

    with open("output.md", "w") as f:
        f.write(text)

    print(text)

run()
