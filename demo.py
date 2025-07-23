# demo.py — Toylogue v2.1 Demo
# ----------------------------
# ✅ YAML — Grammar loaded from YAML file (rule system)
# ✅ JSON — Grammar rules exported for interoperability
# ✅ spaCy — Token-based syntactic and dependency parsing
# ✅ NLTK — Generative CFG tree demo from scratch
# ✅ Prolog — Logical role-tone constraint validation
# ✅ Natural Language Processing — Combined symbolic NLP prototype
# ✅ Prototypes — This script exercises the full grammar prototype system
# ----------------------------

from grammar_engine import (
    load_grammar_yaml,          # ✅ YAML
    generate_phrase,            # ✅ Prototype phrase generation
    analyze_with_spacy,         # ✅ spaCy (NLP)
    demo_cfg_parser,            # ✅ NLTK
    is_valid_combo,             # ✅ Prolog
    export_grammar_to_json      # ✅ JSON
)

# Load rules from YAML file (structured grammar)
rules = load_grammar_yaml()  # ✅ YAML

# Generate a phrase using structured constraints (role/tone/emotion)
phrase = generate_phrase(
    rules,
    role="villain",
    tone="angry",
    name="Lena",
    emotion="furious",
    verb="strike back",
    exclamation="now"
)

print("Generated Phrase:")
print(phrase)

# Analyze phrase with spaCy for tokenization, POS, and dependency parsing
print("\nspaCy Analysis:")  # ✅ spaCy
print(analyze_with_spacy(phrase))  # ✅ Natural language processing

# Parse a CFG tree using NLTK
print("\nCFG Tree(s):")  # ✅ NLTK generative grammar modeling
for tree in demo_cfg_parser():
    tree.pretty_print()

# Validate role-tone compatibility using Prolog
print("\nIs valid combo (villain, angry)?")  # ✅ Prolog rule check
print(is_valid_combo("villain", "angry"))

# Export current grammar rules to JSON
export_grammar_to_json()  # ✅ JSON export
print("\nGrammar rules exported to data/phrases.json")
