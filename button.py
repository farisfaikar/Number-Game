import pygame
import numbergame
import timer
from constantvar import *
import globalvar


class Button:
    def __init__(self, text, width, height, pos, top_color, bottom_color):
        # Core attributes
        self.pressed = False
        self.elevation = 4
        self.dynamic_elevation = self.elevation
        self.original_y_pos = pos[1]
        self.text = text
        self.pos = pos

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
        user_input_length = len(globalvar.num_input)
        if user_input_length < 4:
            if globalvar.num_input.find(self.text) == -1:
                globalvar.num_input += self.text
                globalvar.error_message = ""
            else:
                globalvar.error_message = "You can only input different numbers"
        else:
            globalvar.error_message = "You can only input up to 4 digits"


class ConfirmButton(Button):
    def button_action(self):
        if len(globalvar.num_input) == 4:
            if globalvar.game_state == 'main_game':
                numbergame.compare()
            globalvar.num_input = ""
            globalvar.error_message = ""
        else:
            globalvar.error_message = "You need to input 4 numbers"


class ResetButton(Button):
    def button_action(self):
        globalvar.num_input = ""


class RestartButton(Button):
    def button_action(self):
        numbergame.restart()
        timer.reset_timer()
        globalvar.game_state = 'main_game'

        # error_message shall be eradicated
        globalvar.error_message = ""


class HighscoreButton(Button):
    def button_action(self):
        timer.stop_timer()
        globalvar.game_state = 'highscore'


class AchievementButton(Button):
    def button_action(self):
        print("Display Achievements")
        globalvar.game_state = 'achievement'
