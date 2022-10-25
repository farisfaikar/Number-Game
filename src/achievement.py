import json

from achievement_notif import achv_notif
from globalvar import MAX_ATTEMPTS


def check_achievements(seconds, minutes, atmpts):
    data_json = open("data.json", "r")
    data_json_object = json.load(data_json)
    data_json.close()
    achivements = data_json_object["achievement"]
    achivements["achv01"] = "X"
    achv_notif(1)
    if int(minutes) <= 1:
        achivements["achv02"] = "X"
        achv_notif(2)
    if int(seconds) <= 10:
        achivements["achv03"] = "X"
        achv_notif(3)
    if int(atmpts) == MAX_ATTEMPTS:
        achivements["achv04"] = "X"
        achv_notif(4)
    data_json = open("data.json", "w")
    json.dump(data_json_object, data_json)
    data_json.close()


def load_achievement():
    try:
        with open("data.json", "r") as data:
            achievement = json.load(data)
            return achievement["achievement"]
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
