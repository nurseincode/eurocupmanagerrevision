import json

def load_matches():
    try:
        with open('matches.json') as file:
            matches = json.load(file)

        return matches
    except FileNotFoundError: 
        print('Error: The file "matches.json" does not exist!')
        return []

    # except Exception as e:
    #     print(f'An unexpected error occured: {e}')
    #     return[]
