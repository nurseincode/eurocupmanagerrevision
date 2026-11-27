import json

def load_matches():
    with open('matches.json') as file:
        matches = json.load(file)

    return matches