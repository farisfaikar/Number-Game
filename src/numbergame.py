import json
import random

import globalvar as gv
from achievement import check_achievements


def gen_secret_num():
    while len(gv.secret_num) != 4:
        r_num = str(random.randint(0, 9))
        if r_num in gv.secret_num:
            continue
        else:
            gv.secret_num = gv.secret_num + r_num
    # print(f"DEBUG: secret num = {gv.secret_num}")  # debug: print out secret number


def compare():
    _entered_num = gv.num_input
    _correct_num = 0
    _correct_pos = 0

    if _entered_num == gv.secret_num:
        gv.game_state = "won"
        check_achievements(gv.seconds, gv.minutes, gv.remaining_attempts)
    else:
        for letter in _entered_num:
            letter_index = _entered_num.find(letter)
            if letter == gv.secret_num[letter_index]:
                _correct_num += 1
                _correct_pos += 1
            elif _entered_num[letter_index] in gv.secret_num:
                _correct_num += 1
        gv.attempts += 1
        gv.remaining_attempts = gv.MAX_ATTEMPTS - gv.attempts
        if gv.attempts >= gv.MAX_ATTEMPTS:
            gv.game_state = "lost"

        gv.combinations.append(_entered_num)
        gv.correct_num.append(_correct_num)
        gv.correct_pos.append(_correct_pos)

    gv.is_compared = True


def restart():
    gv.correct_num = []
    gv.correct_pos = []
    gv.combinations = []
    gv.attempts = 0
    gv.game_state = "main_game"
    gv.remaining_attempts = gv.MAX_ATTEMPTS
    gv.secret_num = ""
    gv.text_input = ""

    gen_secret_num()
