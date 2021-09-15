import pygame
from numbergame import Game

# Font
chary_font = 'chary___.ttf'
# Color RGB
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
L_GREY = (100, 100, 100)
XL_GREY = (150, 150, 150)
D_GREY = (25, 25, 25)
WHITE = (255, 255, 255)
BLUE = (150, 150, 255)
D_BLUE = (100, 100, 200)
CYAN = (150, 255, 255)
GREEN = (150, 255, 150)
RED = (255, 150, 150)
YELLOW = (255, 255, 150)
PURPLE = (255, 0, 255)
# User Input
user_input = ''
attempts = 0
correct_num = []
correct_pos = []
combinations = []


class Button:
    def __init__(self, text, width, height, pos, top_color, bottom_color):
        # Core attributes
        self.pressed = False
        self.elevation = 5
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

        # ghost rectangle
        self.ghost_rect = pygame.Rect(pos, (width, height))
        self.ghost_color = XL_GREY  # this color should be the same as the background rect color (ghetto solution)

        # transparent rectangle
        # self.trans_rect = pygame.Surface((width, height))
        # self.trans_rect.set_alpha(128)  # set transparency
        # self.trans_rect.fill(YELLOW)

        # text
        gui_font = pygame.font.Font(chary_font, 20)
        self.text_surf = gui_font.render(self.text, True, BLACK)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.ghost_rect.y = self.original_y_pos - self.elevation

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.ghost_color, self.ghost_rect, border_radius=5)
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=5)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=5)

        # screen.blit(self.trans_rect, self.pos)

        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.ghost_rect.collidepoint(mouse_pos):
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
        user_input_length = len(user_input)
        if user_input_length < 4:
            if user_input.find(self.text) == -1:
                user_input += self.text
            else:
                print("You can only input different numbers")
                # print_error_message()


class ConfirmButton(Button):
    def __init__(self, text, width, height, pos, top_color, bottom_color):
        super().__init__(text, width, height, pos, top_color, bottom_color)
        self.game = Game()

    def button_action(self):
        global attempts
        global user_input
        global correct_num
        global correct_pos
        global combinations

        if len(user_input) == 4:
            self.game.compare()
            attempts = self.game.attempts
            correct_num = self.game.correct_num
            correct_pos = self.game.correct_pos
            combinations = self.game.combinations
            user_input = ""


class ResetButton(Button):
    def button_action(self):
        global user_input
        user_input = ""
