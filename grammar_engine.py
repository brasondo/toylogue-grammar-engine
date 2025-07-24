# grammar_engine.py — Toylogue v3.1 Grammar Engine (Job-Targeted)
# ---------------------------------------------------
# Demonstrates job-aligned grammar-centric NLP tools:
# - Modular grammar system (YAML)
# - JSON export for tools/prompts
# - Prolog constraints for logic validation
# - spaCy for syntactic introspection
# - NLTK for generative grammar structure
# ---------------------------------------------------

import yaml  # Grammar loading
import json  # Grammar export
import random
from nltk import CFG, ChartParser  # Grammar modeling
import requests

import spacy  # NLP analysis
import subprocess

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback: shell out to download spaCy model
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"],
                   check=True)
    nlp = spacy.load("en_core_web_sm")


# ---------------- Load + Export Grammar ---------------- #
def load_grammar_yaml(path='data/phrases.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)['rules']


def export_grammar_to_json(yaml_path='data/phrases.yaml',
                           json_path='data/phrases.json'):
    rules = load_grammar_yaml(yaml_path)
    with open(json_path, 'w') as file:
        json.dump({'rules': rules}, file, indent=2)


# ---------------- Recursive Rule Expansion ---------------- #
def recursive_generate(rules, symbol="S"):
    candidates = [r for r in rules if r["lhs"] == symbol]
    if not candidates:
        return symbol
    rule = random.choice(candidates)
    rhs = rule["rhs"]
    nonterminals = {r['lhs'] for r in rules}
    if all(t not in nonterminals for t in rhs):
        return random.choice(rhs)
    return " ".join(recursive_generate(rules, t) for t in rhs)


# ---------------- Ollama LLM Realization ---------------- #
def surface_realize_with_ollama(structure, role=None):
    prompt = f"""
You are a {role} character who speaks clearly and concisely.
Rewrite the following line to sound natural and expressive but keep it brief (around 2 sentences):

{structure}
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "max_tokens": 50,
                "stream": False
            },
            timeout=10,
        )
        data = response.json()
        if "response" not in data:
            print("⚠️ Unexpected Ollama response:", data)
            return "[Ollama failed]"
        return data["response"].strip()
    except requests.RequestException as exc:
        print("⚠️ Could not reach Ollama:", exc)
        return structure


# ---------------- Prolog Logic Constraints ---------------- #
def is_valid_combo(role, tone):
    try:
        from pyswip import Prolog  # Imported here to avoid dependency unless used (Logic Engine)
    except Exception as exc:  # noqa: BLE001
        print("⚠️ Prolog not available:", exc)
        return False
    prolog = Prolog()
    prolog.assertz("valid(hero, brave)")
    prolog.assertz("valid(villain, angry)")
    prolog.assertz("valid(mentor, calm)")
    prolog.assertz("valid(goofball, silly)")
    result = list(prolog.query(f"valid({role}, {tone})"))
    return bool(result)


# ---------------- spaCy Syntax Analysis ---------------- #
def analyze_with_spacy(text):
    doc = nlp(text)
    return [(t.text, t.pos_, t.dep_) for t in doc]


# ---------------- NLTK Grammar Tree Demo ---------------- #
def demo_cfg_parser():
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> 'Lena' | 'Jamie'
        VP -> V ADJP
        V -> 'is' | 'feels'
        ADJP -> 'furious' | 'worried'
    """)
    parser = ChartParser(grammar)
    return [tree for tree in parser.parse(['Lena', 'feels', 'furious'])]


# ---------------- High-Level Generation API ---------------- #
def generate_line(role="hero",
                  context=None,
                  use_llm=False,
                  rules_path='data/phrases.yaml'):
    """Generate a single line for a role and optional context.

    Parameters
    ----------
    role : str
        Character archetype such as "hero" or "villain".
    context : str, optional
        Event context like "picked_up" or "hugged" used to prefix the line.
    use_llm : bool, default False
        If True, pass the result through Ollama for expressive realization.
    rules_path : str
        YAML path for grammar rules.
    """

    rules = load_grammar_yaml(rules_path)
    symbol = f"S_{role.upper()}"
    line = recursive_generate(rules, symbol=symbol)

    event_prefixes = {
        "picked_up": [
            "Up we go!",
            "Whoa! Thanks for picking me up!",
            "Adventure time!",
        ],
        "hugged": [
            "Aww, hugs make me stronger!",
            "So cozy!",
            "You're the best hugger!",
        ],
        "smile_detected": [
            "I see that smile!",
            "Your smile is contagious!",
            "Happy vibes activated!",
        ],
    }

    if context in event_prefixes:
        prefix = random.choice(event_prefixes[context])
        line = f"{prefix} {line}"

    if use_llm:
        line = surface_realize_with_ollama(line, role=role)

    return line
