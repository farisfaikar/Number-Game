import json
from operator import itemgetter


def save_hs(highscore):
    with open('highscore.json', 'w') as hs_file:
        json.dump(highscore, hs_file)


def load_hs():
    try:
        with open('highscore.json', 'r') as hs_file:
            highscore = json.load(hs_file)
    except FileNotFoundError:
        return []
    return sorted(highscore, key=itemgetter(1), reverse=False)
