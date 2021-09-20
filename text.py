import pygame
import button
import numbergame
from colorpalette import *

# Font
chary_font = 'chary___.ttf'
# Time
elapsed_time = 0


class Rect:
    @staticmethod
    def draw_ui_rect(screen):
        pygame.draw.rect(screen, L_GREY, (0, 0, 800, 170))  # 'screen' rect
        pygame.draw.rect(screen, XL_GREY, (670, 170, 280, 300))  # 'calculator' rect


class Text:
    def __init__(self):
        self.screen = None
        self.text_space = 20
        self.textX = 10  # initial x position
        self.textY = 175  # initial y position
        self.textY_addable = 0
        self.reset_text_y_pos()

    def draw_text(self, screen):
        self.screen = screen
        # Add text
        self.add_line(f"Enter your guess! You have {numbergame.remaining_attempts} attempts left", WHITE)
        self.add_custom_line("Restart", BLUE, 50, 10)

        self.print_error_message()
        self.print_clue_texts()
        self.print_win_message()

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

    def print_error_message(self):
        if len(button.error_message) != 0:
            error_message = f"ERROR: {button.error_message}"
            self.add_line(error_message, RED)
        else:
            self.add_line("", RED)

    def print_clue_texts(self):
        attempts = numbergame.attempts
        correct_num = numbergame.correct_num
        correct_pos = numbergame.correct_pos
        combinations = numbergame.combinations

        for i in range(attempts):
            self.add_line(f"> Attempt #{i + 1}: ({combinations[i]}) {correct_num[i]} correct numbers, "
                          f"{correct_pos[i]} correct pos", CYAN)

    def print_win_message(self):
        is_win = numbergame.is_win
        is_lost = numbergame.is_lost

        if is_win:
            self.add_line("You win!", GREEN)
        if is_lost:
            self.add_line("You have reached the maximum attempt! You lost", RED)
        if is_win or is_lost:
            self.add_line("Hit the restart button to play again", BLUE)


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
