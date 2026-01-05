import os
import re
from datetime import date
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

README_FILE = "README.md"

prompt = f"""
Write a short daily update for my GitHub README.
Date: {date.today()}
Style: concise, technical, optimistic.
Max 3 sentences.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

new_text = response.output_text.strip()

with open(README_FILE, "r") as f:
    content = f.read()

updated_content = re.sub(
    r"(<!-- AI-UPDATE-START -->)(.*?)(<!-- AI-UPDATE-END -->)",
    rf"\1\n{new_text}\n\3",
    content,
    flags=re.DOTALL
)

with open(README_FILE, "w") as f:
    f.write(updated_content)
