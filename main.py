import os
import requests
from bs4 import BeautifulSoup
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------------------
# 1. 抓取真实 Open Call（示例：Res Artis）
# ---------------------------
def fetch_opportunities():
    url = "https://resartis.org/open-calls/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    items = []

    for h in soup.find_all("h2")[:10]:
        items.append(h.get_text())

    return "\n".join(items)


# ---------------------------
# 2. Gemini筛选
# ---------------------------
def analyze(text):
    prompt = f"""
You are an assistant filtering real artist opportunities.

Only keep:
- funded residencies
- grants
- awards
- low/no application fee

Text:
{text}

Return top 5 structured opportunities:
Name / Type / Country / Why relevant
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    res = requests.post(url, json=payload).json()

    try:
        return res["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return str(res)


# ---------------------------
# 3. 主流程
# ---------------------------
def run():
    raw = fetch_opportunities()
    result = analyze(raw)

    with open("output.md", "w") as f:
        f.write(result)

    print(result)


run()
