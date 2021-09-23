import pygame
import button
import numbergame
from colorpalette import *
import timer

# Font
chary_font = 'chary___.ttf'


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

        if button.text_id["clue_text"]:
            self.print_clue_texts()
        elif button.text_id["highscore"]:
            self.print_highscores()

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

        self.add_line(f"Guess the 4 digit number combination! You have {numbergame.remaining_attempts} attempts left", WHITE)

        for i in range(attempts):
            self.add_line(f"> Attempt #{i + 1}: {correct_num[i]} correct numbers, "
                          f"{correct_pos[i]} are in the correct position. [{combinations[i]}]", CYAN)

        self.print_win_message()

    def print_win_message(self):
        is_win = numbergame.is_win
        is_lost = numbergame.is_lost

        if is_win:
            self.add_line(f"You win! The correct number was {numbergame.secret_num}", GREEN)
        if is_lost:
            self.add_line(f"You have run out of attempt! You lost. The correct number was {numbergame.secret_num}", RED)
        if is_win or is_lost:
            self.add_line("Press the restart button to play again", BLUE)
            timer.stop_timer()

    def print_highscores(self):
        self.add_line("Highscores!", YELLOW)
        self.add_line("#1: Faris          - Time: 01:07", WHITE)
        self.add_line("#2: -----          - Time: --:--", WHITE)
        self.add_line("#3: -----          - Time: --:--", WHITE)
        self.add_line("#4: -----          - Time: --:--", WHITE)
        self.add_line("#5: -----          - Time: --:--", WHITE)
        self.add_line("#6: -----          - Time: --:--", WHITE)
        self.add_line("#7: -----          - Time: --:--", WHITE)
        self.add_line("#8: -----          - Time: --:--", WHITE)
        self.add_line("#9: -----          - Time: --:--", WHITE)


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
        text_surf = chary.render(button.user_input, True, self.text_color)
        text_rect = text_surf.get_rect(center=rect.center)

        # draw rect
        pygame.draw.rect(screen, self.box_color, rect)
        # draw text
        screen.blit(text_surf, text_rect)
