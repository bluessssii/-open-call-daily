import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def run():
    if not API_KEY:
        raise Exception("Missing GEMINI_API_KEY")

    prompt = """
You are an assistant that lists 5 international art open calls.

Rules:
- funding preferred
- avoid long residency
- no application fees preferred
- Japan and France allowed if funded

Return structured list:
Name / Country / Type / Deadline / Why relevant
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    r = requests.post(url, json=payload)
    data = r.json()

    # 🧠 强防御：打印原始返回（关键）
    print("RAW RESPONSE:", data)

    # ❗ 防止 candidates 空
    if "candidates" not in data or not data["candidates"]:
        raise Exception("No candidates returned from Gemini")

    text = data["candidates"][0]["content"]["parts"][0]["text"]

    with open("output.md", "w") as f:
        f.write(text)

    print(text)

run()
