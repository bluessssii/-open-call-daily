import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

print("GEMINI KEY:", API_KEY)

def run():
    if not API_KEY:
        raise Exception("GEMINI_API_KEY not found")

    prompt = "Give 3 art open calls"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    r = requests.post(url, json=payload)
    data = r.json()

    print(data)

    text = data["candidates"][0]["content"]["parts"][0]["text"]

    with open("output.md", "w") as f:
        f.write(text)

    print(text)

run()
