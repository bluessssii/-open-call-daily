import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")


def generate():
    prompt = """
Return 5 international contemporary art open calls.

Format:
Name / Country / Type / Deadline / 1-line description

Focus on:
- funded opportunities
- residencies
- awards
- exhibitions
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    r = requests.post(url, json=payload)
    data = r.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return str(data)


def send_email(content):
    url = "https://api.resend.com/emails"

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "from": "OpenCall Bot <onboarding@resend.dev>",
        "to": EMAIL_TO,
        "subject": "Daily Open Call Digest",
        "text": content
    }

    requests.post(url, json=payload, headers=headers)


def run():
    content = generate()
    send_email(content)
    print(content)


if __name__ == "__main__":
    run()
