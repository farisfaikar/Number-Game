import json
import globalvar as gv
from operator import itemgetter
import pathlib

DATA_JSON_PATH = pathlib.Path("data.json")


def check_if_data_exists():
    if not DATA_JSON_PATH.exists():
        default = {"highscore": [], "achievement":
                    {"achv01": " ", "achv02": " ", "achv03": " ", "achv04": " ", 
                    "achv05": " ", "achv06": " ", "achv07": " "}}
        with open(DATA_JSON_PATH, 'w') as file:
            json.dump(default, file, indent=2)


def save_hs(data_json):
    with open(DATA_JSON_PATH, 'w') as hs_file:
        json.dump(data_json, hs_file, indent=2)


def load_hs():
    with open(DATA_JSON_PATH, 'r') as hs_file:
        return json.load(hs_file)


def save_score():
    data_json = load_hs()
    highscore = data_json["highscore"]
    highscore.append([gv.text_input, gv.lapped_time])
    data_json["highscore"] = sorted(data_json["highscore"], key=itemgetter(1), reverse=False)
    save_hs(data_json)