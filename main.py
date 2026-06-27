import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run():
    prompt = """
You are an assistant that finds international art open calls.

Focus rules:
- Prefer funding / grants / cash awards
- Avoid long residency requirements
- Japan & France allowed if funded
- Avoid application fees if possible

Return 5 opportunities in structured list format:
Name / Country / Type / Deadline / Why relevant
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    with open("output.md", "w") as f:
        f.write(output)

    print(output)

if __name__ == "__main__":
    run()
