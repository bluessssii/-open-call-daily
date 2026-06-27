import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def generate_open_calls():
    prompt = """
You are an assistant that finds international contemporary art open calls.

Return 5 items only.

Each item must include:
- Name
- Country
- Type (residency / grant / award / exhibition)
- Deadline (if available)
- Why it is relevant to experimental / conceptual / research-based art practices

Focus on:
- funded opportunities
- low application burden
- conceptual / research / media art friendly

Do NOT include vague or commercial listings.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    r = requests.post(url, json=payload)

    data = r.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return str(data)


def save_output(text):
    with open("output.md", "w") as f:
        f.write(text)


def run():
    result = generate_open_calls()
    save_output(result)
    print(result)


if __name__ == "__main__":
    run()
