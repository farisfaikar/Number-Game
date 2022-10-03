import json
from operator import itemgetter

import globalvar as gv


def check_if_data_exists():
    try:
        with open("data.json", "r") as hs_file:
            hs_file.close()
    except FileNotFoundError:
        default = {
            "highscore": [],
            "achievement": {
                "achv01": " ",
                "achv02": " ",
                "achv03": " ",
                "achv04": " ",
                "achv05": " ",
                "achv06": " ",
                "achv07": " ",
            },
        }
        with open("data.json", "w") as f:
            json.dump(default, f, indent=2)
        f.close()


def save_hs(data_json):
    with open("data.json", "w") as hs_file:
        json.dump(data_json, hs_file, indent=2)
    hs_file.close()


def load_hs():
    with open("data.json", "r") as hs_file:
        data_json = json.load(hs_file)
    hs_file.close()
    return data_json


def save_score():
    data_json = load_hs()
    highscore = data_json["highscore"]
    highscore.append([gv.text_input, gv.lapped_time])
    data_json["highscore"] = sorted(
        data_json["highscore"], key=itemgetter(1), reverse=False
    )
    save_hs(data_json)
