import random
import button

correct_num = []
correct_pos = []
combinations = []
attempts = 0
remaining_attempts = 0


class Game:
    secret_num = ''
    MAX_ATTEMPTS = 8

    def gen_secret_num(self):
        while len(self.secret_num) != 4:
            r_num = str(random.randint(0, 9))
            if r_num in self.secret_num:
                continue
            else:
                self.secret_num = self.secret_num + r_num

    def compare(self):
        self.gen_secret_num()

        secret_num = self.secret_num
        entered_num = button.user_input
        correct_num_ = 0
        correct_pos_ = 0

        global attempts
        global remaining_attempts

        if entered_num == secret_num:
            print("You win!")
        else:
            for letter in entered_num:
                letter_index = entered_num.find(letter)
                if letter == secret_num[letter_index]:
                    correct_num_ += 1
                    correct_pos_ += 1
                elif entered_num[letter_index] in secret_num:
                    correct_num_ += 1
            attempts += 1
            remaining_attempts = self.MAX_ATTEMPTS - attempts
            if attempts >= self.MAX_ATTEMPTS:
                print("You have reached the maximum attempt! You lost")

            combinations.append(entered_num)
            correct_num.append(correct_num_)
            correct_pos.append(correct_pos_)
