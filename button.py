import pygame
import numbergame
from numbergame import Game
from colorpalette import *

# Font
chary_font = 'chary___.ttf'
# User Input
user_input = ""
attempts = 0
correct_num = []
correct_pos = []
combinations = []
error_message = ""


class Button:
    def __init__(self, text, width, height, pos, top_color, bottom_color):
        # Core attributes
        self.pressed = False
        self.elevation = 5
        self.dynamic_elevation = self.elevation
        self.original_y_pos = pos[1]
        self.text = text
        self.pos = pos

        # Initiate game
        self.game = Game()

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.TOP_COLOR = top_color
        self.top_color = top_color

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = bottom_color

        # hitbox rectangle
        self.hitbox_rect = pygame.Rect(pos, (width, height))

        # text
        gui_font = pygame.font.Font(chary_font, 20)
        self.text_surf = gui_font.render(self.text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.hitbox_rect.y = self.original_y_pos - self.elevation

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=5)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=5)

        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.hitbox_rect.collidepoint(mouse_pos):
            self.top_color = WHITE
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed is True:
                    self.button_action()
                    self.pressed = False
        else:
            self.pressed = False
            self.dynamic_elevation = self.elevation
            self.top_color = self.TOP_COLOR

    def button_action(self):
        global user_input
        global error_message
        user_input_length = len(user_input)
        if user_input_length < 4:
            if user_input.find(self.text) == -1:
                user_input += self.text
                error_message = ""
            else:
                error_message = "You can only input different numbers"
        else:
            error_message = "You can only input up to 4 digits"


class ConfirmButton(Button):
    def button_action(self):
        global user_input
        global error_message

        if len(user_input) == 4:
            if not numbergame.is_win and not numbergame.is_lost:
                self.game.compare()
            user_input = ""
            error_message = ""
        else:
            error_message = "You need to input 4 numbers"


class ResetButton(Button):
    def button_action(self):
        global user_input
        user_input = ""


class RestartButton(Button):
    def button_action(self):
        self.game.restart()
        global error_message
        error_message = ""


class HighscoreButton(Button):
    def button_action(self):
        print("display highscore")
