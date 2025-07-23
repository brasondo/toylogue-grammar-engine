import yaml
import random

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
