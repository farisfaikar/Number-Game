import random
import button
import text

# numbergame variables
correct_num = []
correct_pos = []
combinations = []
attempts = 0
MAX_ATTEMPTS = 8
remaining_attempts = MAX_ATTEMPTS
secret_num = ""
game_state = 'main_game'  # game_state types: 'main_game', 'lost', 'won', 'highscore', 'achievement'


def gen_secret_num():
    global secret_num

    while len(secret_num) != 4:
        r_num = str(random.randint(0, 9))
        if r_num in secret_num:
            continue
        else:
            secret_num = secret_num + r_num


def compare():
    gen_secret_num()

    global secret_num
    global attempts
    global remaining_attempts
    global game_state
    # print(secret_num)  # debug: print out secret number

    entered_num = button.num_input
    correct_num_ = 0
    correct_pos_ = 0

    if entered_num == secret_num:
        game_state = 'won'
    else:
        for letter in entered_num:
            letter_index = entered_num.find(letter)
            if letter == secret_num[letter_index]:
                correct_num_ += 1
                correct_pos_ += 1
            elif entered_num[letter_index] in secret_num:
                correct_num_ += 1
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        if attempts >= MAX_ATTEMPTS:
            game_state = 'lost'

        combinations.append(entered_num)
        correct_num.append(correct_num_)
        correct_pos.append(correct_pos_)


def restart():
    global correct_num
    global correct_pos
    global combinations
    global attempts
    global remaining_attempts
    global secret_num
    global game_state

    correct_num = []
    correct_pos = []
    combinations = []
    attempts = 0
    game_state = 'main_game'
    remaining_attempts = MAX_ATTEMPTS
    secret_num = ''
    gen_secret_num()
    text.text_input = ""
