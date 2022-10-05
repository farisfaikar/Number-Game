import json
from operator import itemgetter
import globalvar as gv


class Achievement:
    @staticmethod
    def save(highscore):
        with open('data.json', 'w') as hs_file:
            json.dump(highscore, hs_file, indent=2)

    @staticmethod
    def load():
        try:
            with open('highscore.json', 'r') as hs_file:
                highscore = json.load(hs_file)
        except FileNotFoundError:
            return []
        return sorted(highscore, key=itemgetter(1), reverse=False)

    @staticmethod
    def save_score():
        highscore = Achievement.load()
        highscore.append([gv.text_input, gv.lapped_time])
        Achievement.save(sorted(highscore, key=itemgetter(1), reverse=False))


class Highscore:
    @staticmethod
    def save():
        pass

    @staticmethod
    def load():
        pass


"""
{
  "highscore": [
    ["Faris", 100],
    ["Fadel", 200],
    ["Fadel", 200]
  ],
  "achievement": {
    "achv01": false,
    "achv02": false,
    "achv03": false,
    "achv04": false,
    "achv05": false,
    "achv06": false,
    "achv07": false
  }
}
"""
