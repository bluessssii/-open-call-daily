import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")


def generate():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [{"text": "Return 5 international art open calls with name, country, deadline."}]
            }
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
        "from": "onboarding@resend.dev",
        "to": EMAIL_TO,
        "subject": "Daily Open Call Digest",
        "text": content
    }

    response = requests.post(url, json=payload, headers=headers)

    # 🧠 关键：必须看到返回值
    print("EMAIL STATUS:", response.status_code)
    print("EMAIL RESPONSE:", response.text)

    return response.text


def run():
    content = generate()
    print("GEMINI OUTPUT:", content)

    send_email(content)


if __name__ == "__main__":
    run()
