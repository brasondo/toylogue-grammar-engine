import yaml
import random

def load_grammar(path='data/phrases.yaml'):
    """
    Load grammar rules from a YAML file.
    
    :param path: Path to the YAML file containing grammar rules.
    :return: A dictionary containing the grammar rules.
    """
    with open(path, 'r') as file:
        grammar = yaml.safe_load(file)['rules']
    return grammar

def generate_phrase(rules, role, tone, name, emotion, verb='retaliate', exclamation='Wow'):
    # Find rules that match the given role and tone
    matching = [
        r for r in rules
        if role in r['constraints']['role'] and tone in r['constraints']['tone']
    ]

    if not matching:
        raise ValueError(f"No matching rules found for role '{role}' and tone '{tone}'")
    
    # Randomly select a rule from the matching ones
    selected_rule = random.choice(matching)
    phrase = selected_rule['structure']

    # Replace placeholders with actual values
    phrase = phrase.replace("[GREETING]", random.choice(["Hi", "Hey", "Hello"]))
    phrase = phrase.replace("[NAME]", name)
    phrase = phrase.replace("[EMOTION]", emotion)
    phrase = phrase.replace("[VERB]", verb)
    phrase = phrase.replace("[EXCLAMATION]", exclamation)

    return phrase