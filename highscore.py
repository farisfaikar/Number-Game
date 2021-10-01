import json
import text
import globalvar as gv
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


def save_score():
    highscore = load_hs()
    player_name = gv.text_input
    norm_player_name = text.normalize_text(player_name)
    highscore.append([norm_player_name, gv.lapped_time])
    save_hs(sorted(highscore, key=itemgetter(1), reverse=False))
