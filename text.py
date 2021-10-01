import pygame
import button
import numbergame
import timer
import highscore as hs
from globalvar import *

text_input = ""


def normalize_text(text_):
    max_text_length = 5
    text_length = len(text_)
    if text_length < 5:
        for i in range(max_text_length - text_length):
            text_ += " "
        return text_
    else:
        return text_


class Text:
    def __init__(self):
        self.screen = None
        self.text_space = 20
        self.textX = 10  # initial x position
        self.textY = 5  # initial y position
        self.textY_addable = 0
        self.reset_text_y_pos()

    def draw_text(self, screen):
        self.screen = screen
        # Add text
        self.print_time()
        game_state = numbergame.game_state
        if game_state == 'main_game' or game_state == 'won' or game_state == 'lost':
            self.print_clue_texts()
        elif game_state == 'highscore':
            self.print_highscores()

        if game_state == 'won':
            self.input_player_name()

        self.reset_text_y_pos()

    def add_line(self, text, color):
        # Hard-coded font
        chary = pygame.font.Font(chary_font, 20)
        # Render text
        line = chary.render(text, True, color)
        self.textY_addable = self.textY_addable + self.text_space
        self.screen.blit(line, (self.textX, self.textY_addable))

    def add_custom_line(self, text, color, x, y):
        # Hard-coded font
        chary = pygame.font.Font(chary_font, 20)
        # Render text
        line = chary.render(text, True, color)
        self.screen.blit(line, (x, y))

    def reset_text_y_pos(self):
        self.textY_addable = self.textY - self.text_space

    def print_time(self):
        self.add_custom_line(f"Timer: {timer.minutes}:{timer.seconds}", WHITE, 680, 5)

    def print_error_message(self):
        if len(button.error_message) != 0:
            error_message = f"ERROR: {button.error_message}"
            self.add_custom_line(error_message, RED, 10, 5)
        else:
            self.add_custom_line("", RED, 10, 155)

    def print_clue_texts(self):
        attempts = numbergame.attempts
        correct_num = numbergame.correct_num
        correct_pos = numbergame.correct_pos
        combinations = numbergame.combinations

        self.add_line(f"Guess the 4 digit number combination! You have {numbergame.remaining_attempts} "
                      + "attempts left", WHITE)

        for i in range(attempts):
            self.add_line(f"> Attempt #{i + 1}: {correct_num[i]} correct numbers, "
                          f"{correct_pos[i]} are in the correct position. [{combinations[i]}]", CYAN)

        self.print_win_message()

    def print_win_message(self):
        if numbergame.game_state == 'won':
            self.add_line(f"You win! The correct number was {numbergame.secret_num}", GREEN)
        if numbergame.game_state == 'lost':
            self.add_line(f"You have run out of attempt! You lost. The correct number was {numbergame.secret_num}", RED)
        if numbergame.game_state == 'won' or numbergame.game_state == 'lost':
            self.add_line("Press the restart button to play again", BLUE)
            timer.stop_timer()

    def print_highscores(self):
        max_highscore = 9
        self.add_line("Highscores!", YELLOW)
        # The methods below will be replaced with a for loop
        highscore = hs.load_hs()
        for index, [player_name, player_time] in enumerate(highscore):
            form_player_time = timer.reformat_time(player_time)
            self.add_line(f"#{index + 1}: {player_name}          - Time: {form_player_time}", WHITE)

        highscore_size = len(highscore)
        if highscore_size < max_highscore:
            for i in range(max_highscore - highscore_size):
                self.add_line(f"#{i + highscore_size + 1}: -----          - Time: --:--", WHITE)

    def input_player_name(self):
        self.add_line(f"Enter your name! (5 letters): {text_input}", YELLOW)


class TextBox:
    def __init__(self, width, height, pos, box_color, text_color):
        self.width = width
        self.height = height
        self.pos = pos
        self.box_color = box_color
        self.text_color = text_color

    def draw(self, screen):
        # create textbox
        rect = pygame.Rect(self.pos, (self.width, self.height))
        chary = pygame.font.Font(chary_font, 20)
        text_surf = chary.render(button.num_input, True, self.text_color)
        text_rect = text_surf.get_rect(center=rect.center)

        # draw rect
        pygame.draw.rect(screen, self.box_color, rect)
        # draw text
        screen.blit(text_surf, text_rect)
