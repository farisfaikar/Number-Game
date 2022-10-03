import json

from globalvar import MAX_ATTEMPTS


def check_achievements(seconds, minutes, atmpts):
    data_json = open("data.json", "r")
    data_json_object = json.load(data_json)
    data_json.close()
    data_json_object["achievement"]["achv01"] = "X"
    if int(minutes) <= 1:
        data_json_object["achievement"]["achv02"] = "X"
    if int(seconds) <= 10:
        data_json_object["achievement"]["achv03"] = "X"
    if int(atmpts) == MAX_ATTEMPTS:
        data_json_object["achievement"]["achv04"] = "X"
    data_json = open("data.json", "w")
    json.dump(data_json_object, data_json)
    data_json.close()


def load_achievement():
    try:
        with open("data.json", "r") as data:
            achievement = json.load(data)
    except FileNotFoundError:
        return {
            "highscore": [],
            "achievement": {
                "achv01": False,
                "achv02": False,
                "achv03": False,
                "achv04": False,
                "achv05": False,
                "achv06": False,
                "achv07": False,
            },
        }
    return achievement["achievement"]
