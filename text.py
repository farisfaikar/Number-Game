import pygame
import button

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
D_GREEN = (100, 200, 100)
XD_GREEN = (50, 150, 50)
RED = (255, 150, 150)
YELLOW = (255, 255, 150)
PURPLE = (255, 0, 255)
# Time
elapsed_time = 0
# Black display (may need to relocate this variable)
black_display = None


class Rect:
    @staticmethod
    def draw_ui_rect(screen):
        pygame.draw.rect(screen, L_GREY, (0, 0, 800, 145))  # 'screen' rect
        pygame.draw.rect(screen, XL_GREY, (520, 145, 280, 300))  # 'calculator' rect
        global black_display
        black_display = pygame.draw.rect(screen, BLACK, (600, 155, 110, 30))


class Text:
    def __init__(self):
        self.screen = None
        self.text_space = 20
        self.textX = 10  # initial x position
        self.textY = 155  # initial y position
        self.textY_addable = self.textY - self.text_space  # stored y position (is added every time a new line is added)

    def draw_text(self, screen):
        self.screen = screen
        # Add text
        self.add_line("Enter your guess!", WHITE)

        attempts = button.attempts
        correct_num = button.correct_num
        correct_pos = button.correct_pos

        for x in range(attempts):
            self.add_line(f"> Attempt #{x + 1}: ({1234}) {correct_num} correct numbers, "
                          f"{correct_pos} correct pos", CYAN)

        # self.add_line("You win!", GREEN)
        # self.add_line("Do you wish to restart? [y/n]", BLUE)

        # reset textY position
        self.textY_addable = self.textY - self.text_space

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
