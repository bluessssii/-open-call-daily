import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")


def generate():
    prompt = """
You are an assistant that finds 5 high-quality international art open calls.

Focus:
- funded opportunities
- grants / awards
- low application burden

Return structured list:
Name / Country / Type / Deadline / Why relevant
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    r = requests.post(url, json=payload).json()

    return r["candidates"][0]["content"]["parts"][0]["text"]


def send_email(content):
    url = "https://api.resend.com/emails"

    payload = {
        "from": "OpenCall Bot <onboarding@resend.dev>",
        "to": EMAIL_TO,
        "subject": "Daily Open Call Digest",
        "text": content
    }

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    requests.post(url, json=payload, headers=headers)


def run():
    content = generate()

    with open("output.md", "w") as f:
        f.write(content)

    send_email(content)

    print(content)


run()
