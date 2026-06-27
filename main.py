import os
import requests

def run():
    print("START OK")

    api_key = os.getenv("GEMINI_API_KEY")

    print("KEY EXISTS:", bool(api_key))

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    payload = {
        "contents": [{"parts": [{"text": "Say hello"}]}]
    }

    r = requests.post(url, json=payload)

    print("STATUS:", r.status_code)
    print("RAW:", r.text[:500])

run()
