from grammar_engine import load_grammar, generate_phrase

rules = load_grammar()

print(generate_phrase(
    rules,
    role="mentor",
    tone="sad",
    name="Alice",
    emotion="disappointed"))

print(generate_phrase(
    rules,
    role="villain",
    tone="angry",
    name="Lena",
    emotion="furious",
    verb="unleash my power"
))

print(generate_phrase(
    rules,
    role="friend",
    tone="happy",
    name="Kai",
    emotion="excited"
))

print(generate_phrase(
    rules,
    role="coach",
    tone="supportive",
    name="Milo",
    emotion="nervous"
))

print(generate_phrase(
    rules,
    role="mentor",
    tone="excited",
    name="Raya",
    emotion="awesome",
    exclamation="Fantastic"
))