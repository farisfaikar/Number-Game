import random
import text
import globalvar


def gen_secret_num():
    while len(globalvar.secret_num) != 4:
        r_num = str(random.randint(0, 9))
        if r_num in globalvar.secret_num:
            continue
        else:
            globalvar.secret_num = globalvar.secret_num + r_num


def compare():
    gen_secret_num()
    # print(globalvar.secret_num)  # debug: print out secret number

    _entered_num = globalvar.num_input
    _correct_num = 0
    _correct_pos = 0

    if _entered_num == globalvar.secret_num:
        globalvar.game_state = 'won'
    else:
        for letter in _entered_num:
            letter_index = _entered_num.find(letter)
            if letter == globalvar.secret_num[letter_index]:
                _correct_num += 1
                _correct_pos += 1
            elif _entered_num[letter_index] in globalvar.secret_num:
                _correct_num += 1
        globalvar.attempts += 1
        globalvar.remaining_attempts = globalvar.MAX_ATTEMPTS - globalvar.attempts
        if globalvar.attempts >= globalvar.MAX_ATTEMPTS:
            globalvar.game_state = 'lost'

        globalvar.combinations.append(_entered_num)
        globalvar.correct_num.append(_correct_num)
        globalvar.correct_pos.append(_correct_pos)


def restart():
    globalvar.correct_num = []
    globalvar.correct_pos = []
    globalvar.combinations = []
    globalvar.attempts = 0
    globalvar.game_state = 'main_game'
    globalvar.remaining_attempts = globalvar.MAX_ATTEMPTS
    globalvar.secret_num = ''

    gen_secret_num()
    text.text_input = ""
