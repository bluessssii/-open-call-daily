import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")


def generate_open_calls():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Give 5 international art open calls, list clearly."
                    }
                ]
            }
        ]
    }

    r = requests.post(url, json=payload)
    data = r.json()

    print("=== GEMINI RAW ===")
    print(data)

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
        "from": "onboarding@resend.dev",
        "to": EMAIL_TO,
        "subject": "Daily Open Call Digest",
        "text": content
    }

    response = requests.post(url, json=payload, headers=headers)

    # 🧠 关键：你要看的就在这里
    print("=== RESEND STATUS ===")
    print(response.status_code)

    print("=== RESEND BODY ===")
    print(response.text)

    return response.text


def run():
    content = generate_open_calls()
    send_email(content)


if __name__ == "__main__":
    run()
