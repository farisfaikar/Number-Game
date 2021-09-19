import random
import button

correct_num = []
correct_pos = []
combinations = []
attempts = 0
MAX_ATTEMPTS = 8
remaining_attempts = MAX_ATTEMPTS
is_win = False
is_lost = False


class Game:
    secret_num = ''

    def gen_secret_num(self):
        while len(self.secret_num) != 4:
            r_num = str(random.randint(0, 9))
            if r_num in self.secret_num:
                continue
            else:
                self.secret_num = self.secret_num + r_num

    def compare(self):
        self.gen_secret_num()
        # print(f"Secret Number: {self.secret_num}")

        secret_num = self.secret_num
        entered_num = button.user_input
        correct_num_ = 0
        correct_pos_ = 0

        global attempts
        global remaining_attempts
        global is_win
        global is_lost

        if entered_num == secret_num:
            print("You win!")
            is_win = True
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
                is_lost = True

            combinations.append(entered_num)
            correct_num.append(correct_num_)
            correct_pos.append(correct_pos_)

    def restart(self):
        global correct_num
        global correct_pos
        global combinations
        global attempts
        global is_win
        global is_lost
        global remaining_attempts

        correct_num = []
        correct_pos = []
        combinations = []
        attempts = 0
        is_win = False
        is_lost = False
        remaining_attempts = MAX_ATTEMPTS
