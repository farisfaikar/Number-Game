import json


def check_achv01():
    # achv01 = I did it!: Finish the puzzle for the first time
    pass


def load_achievement():
    try:
        with open('data.json', 'r') as data:
            achievement = json.load(data)
    except FileNotFoundError:
        return {"highscore": [],
                "achievement": {
                    "achv01": False,
                    "achv02": False,
                    "achv03": False,
                    "achv04": False,
                    "achv05": False,
                    "achv06": False,
                    "achv07": False
                    }
                }
    return achievement["achievement"]
