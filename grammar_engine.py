# ---------------- Imports ---------------- #
import yaml
import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# ---------------- Configuration ---------------- #
load_dotenv()  # ✅ This loads .env file at runtime 
print("Loaded API key prefix:", os.getenv("OPENAI_API_KEY")[:10]) # (Ensure you have set OPENAI_API_KEY in your .env file)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- YAML I/O ---------------- #
def load_grammar_yaml(path='data/phrases.yaml'):
    with open(path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)['rules']

# ---------------- Recursive Generator ---------------- #
def recursive_generate(rules, symbol="S"):
    candidates = [r for r in rules if r["lhs"] == symbol]

    if not candidates:
        return symbol  # Treat unknown as terminal fallback

    rule = random.choice(candidates)
    rhs = rule["rhs"]

    if symbol.isupper() and all(isinstance(t, str) and t not in [r["lhs"] for r in rules] for t in rhs):
        return random.choice(rhs)

    return " ".join(recursive_generate(rules, token) for token in rhs)


def surface_realize_with_gpt(structure, role=None):
    prompt = f"""
You are a dialogue writer for a toy/game character. The character is a {role}.
Turn the following structured phrase into a natural, expressive sentence:
Structure: "{structure}"
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
