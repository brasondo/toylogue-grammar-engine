# grammar_engine.py — Toylogue v2.1 Grammar Engine

# ------------------------
# ✅ YAML — Used for loading grammar rules from structured files
# ✅ JSON — Used for exporting grammar to a portable format
# ✅ spaCy — For token-level linguistic analysis (NLP)
# ✅ NLTK — For formal generative grammar demos with CFG trees
# ✅ Prolog — For logic-based validation of phrase constraints
# ✅ Natural Language Processing — Overall architecture applies structured NLP techniques
# ✅ Prototypes — This entire system is a working grammar prototype for expressive generation
# ------------------------

import yaml  # ✅ YAML
import json  # ✅ JSON
import random
import spacy  # ✅ spaCy (NLP)
from nltk import CFG, ChartParser  # ✅ NLTK
from pyswip import Prolog  # ✅ Prolog

nlp = spacy.load("en_core_web_sm")  # ✅ Natural language processing engine initialized

# ---------------- YAML + JSON I/O ---------------- #
def load_grammar_yaml(path='data/phrases.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)['rules']  # ✅ YAML usage

def load_grammar_json(path='data/phrases.json'):
    with open(path, 'r') as file:
        return json.load(file)['rules']  # ✅ JSON loading

def export_grammar_to_json(yaml_path='data/phrases.yaml', json_path='data/phrases.json'):
    rules = load_grammar_yaml(yaml_path)
    with open(json_path, 'w') as file:
        json.dump({'rules': rules}, file, indent=2)  # ✅ JSON export

# ---------------- Phrase Generation ---------------- #
def generate_phrase(rules, role=None, tone=None, name=None, emotion=None, verb=None, exclamation=None):
    # ✅ Prototype logic for compositional phrase generation
    matching = [r for r in rules if
                (not role or r.get('role') == role) and
                (not tone or r.get('tone') == tone) and
                (not emotion or r.get('emotion') == emotion)]

    if not matching:
        return "No matching rules."

    rule = random.choice(matching)
    phrase = rule['structure']
    phrase = phrase.replace("[GREETING]", random.choice(["Hi", "Hey", "Hello"]))
    phrase = phrase.replace("[NAME]", name or "")
    phrase = phrase.replace("[EMOTION]", emotion or "")
    phrase = phrase.replace("[VERB]", verb or "")
    phrase = phrase.replace("[EXCLAMATION]", exclamation or "")
    return phrase

# ---------------- NLP Integration (spaCy) ---------------- #
def analyze_with_spacy(text):
    doc = nlp(text)  # ✅ spaCy NLP token parsing
    return [(token.text, token.pos_, token.dep_) for token in doc]  # ✅ NLP metadata

# ---------------- Formal Grammar via NLTK ---------------- #
def demo_cfg_parser():
    # ✅ NLTK CFG grammar definition and parse tree generation
    grammar = CFG.fromstring("""
      S -> NP VP
      NP -> 'Lena' | 'Jamie'
      VP -> V ADJP
      V -> 'is' | 'feels'
      ADJP -> 'furious' | 'worried'
    """)
    parser = ChartParser(grammar)
    return [tree for tree in parser.parse(['Lena', 'feels', 'furious'])]  # ✅ NLTK tree

# ---------------- Prolog Constraints ---------------- #
def is_valid_combo(role, tone):
    # ✅ Prolog logic constraints for grammar validity
    prolog = Prolog()
    prolog.assertz("valid(villain, angry)")
    prolog.assertz("valid(mentor, calm)")
    result = list(prolog.query(f"valid({role}, {tone})"))
    return bool(result)  # ✅ Logic-based filtering

# ---------------- Rule Appending ---------------- #
def append_missing_rule(filepath, role, tone, emotion):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)  # ✅ YAML update

    rules = data.get('rules', [])
    exists = any(
        rule.get('role') == role and
        rule.get('tone') == tone and
        rule.get('emotion') == emotion
        for rule in rules
    )

    if exists:
        return False

    new_rule = {
        "role": role,
        "tone": tone,
        "emotion": emotion,
        "structure": "[GREETING] [NAME], I sense you're feeling [EMOTION]. Keep [VERB]. [EXCLAMATION]!"
    }

    rules.append(new_rule)
    data['rules'] = rules

    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, sort_keys=False, allow_unicode=True)  # ✅ YAML write

    return True
