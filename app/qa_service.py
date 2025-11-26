import json
from pathlib import Path

from .openai_client import client

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "scraped.json"


def load_context() -> str:
    if not DATA_FILE.exists():
        raise RuntimeError("data/scraped.json not found.")

    raw = DATA_FILE.read_text(encoding="utf-8")
    pages = json.loads(raw)

    parts = []
    for page in pages:
        url = page.get("url", "")
        content = page.get("content", "")
        if not content:
            continue
        parts.append(f"URL: {url}\n{content}")

    return "\n\n".join(parts)


def answer_question(question: str) -> str:
    context = load_context()

    system_prompt = (
        "Sa oled abiline, kes vastab ainult tehisintellekt.ee veebilehelt pärit info põhjal. "
        "Kui vastust ei ole võimalik kindlalt leida, ütle ausalt, et infot pole."
    )

    user_content = (
        f"Küsimus: {question}\n\n"
        "Vasta ainult alloleva teksti põhjal:\n\n"
        f"{context}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
