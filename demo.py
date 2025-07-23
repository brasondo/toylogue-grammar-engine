# demo.py — Toylogue v3.3 Character Dialogue Demo
from grammar_engine import load_grammar_yaml, recursive_generate

rules = load_grammar_yaml()

# Choose one of the character archetypes to generate from
for role_symbol in ["S_HERO", "S_VILLAIN", "S_GOOFBALL", "S_MENTOR", "S_REBEL", "S_ROYALTY"]:
    print(f"\n{role_symbol} samples:")
    for _ in range(2):
        print("→", recursive_generate(rules, symbol=role_symbol))