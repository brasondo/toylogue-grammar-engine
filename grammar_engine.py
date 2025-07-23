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
import spacy  # NLP analysis
from nltk import CFG, ChartParser  # Grammar modeling
from pyswip import Prolog  # Logic engine
import requests

nlp = spacy.load("en_core_web_sm")

# ---------------- Load + Export Grammar ---------------- #
def load_grammar_yaml(path='data/phrases.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)['rules']

def export_grammar_to_json(yaml_path='data/phrases.yaml', json_path='data/phrases.json'):
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
    prompt = f"You are a toy character of type '{role}'. Say the following line with expressiveness:\n{structure}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    data = response.json()
    if "response" not in data:
        print("⚠️ Unexpected Ollama response:", data)
        return "[Ollama failed]"
    return data["response"].strip()

# ---------------- Prolog Logic Constraints ---------------- #
def is_valid_combo(role, tone):
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
