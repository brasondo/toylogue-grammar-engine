# demo.py — Toylogue v3.1 (Job-Targeted Demonstration)
# -----------------------------------------------------
# This file demonstrates grammar-centric NLP engineering:
# - Rule-based recursive generation (YAML)
# - Logic constraints (Prolog)
# - Expressive realization (Ollama)
# - Syntactic analysis (spaCy)
# - Formal grammar modeling (NLTK)
# - Data structure export (JSON)
# -----------------------------------------------------

from grammar_engine import (
    load_grammar_yaml,
    recursive_generate,
    surface_realize_with_ollama,
    is_valid_combo,
    analyze_with_spacy,
    demo_cfg_parser,
    export_grammar_to_json,
)

# Load grammar rules (structured, modular grammar)
rules = load_grammar_yaml()

# Demonstrate role-driven recursive generation with LLM realization
archetypes = ["S_HERO", "S_VILLAIN", "S_GOOFBALL", "S_MENTOR", "S_REBEL", "S_ROYALTY"]

for role_symbol in archetypes:
    print(f"\n{role_symbol} samples:")
    for _ in range(1):
        base = recursive_generate(rules, symbol=role_symbol)
        print("Raw:", base)
        refined = surface_realize_with_ollama(base, role=role_symbol.replace("S_", "").lower())
        print("Ollama:", refined)

# Apply symbolic constraint logic via Prolog
print("\nProlog Logic Check:")
print("Is valid combo (villain, angry)?", is_valid_combo("villain", "angry"))
print("Is valid combo (hero, angry)?", is_valid_combo("hero", "angry"))

# Perform spaCy analysis of a generated phrase
sample_text = "I am Voidmaster, ruler of shadows."
print("\nspaCy Analysis of Sample Phrase:")
print(analyze_with_spacy(sample_text))

# Demonstrate formal CFG parse tree (syntactic modeling)
print("\nCFG Parse Tree (NLTK Demo):")
for tree in demo_cfg_parser():
    tree.pretty_print()

# Export grammar rules to JSON for reuse or prompt injection
export_grammar_to_json()
print("\nGrammar exported to data/phrases.json")