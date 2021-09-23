import pygame, sys
from text import Text, TextBox
from button import Button, ConfirmButton, ResetButton, RestartButton, HighscoreButton
from colorpalette import *
import timer


class Program:
    def __init__(self):
        # Enter instances here -----------------------------------------------------
        self.text = Text()

        self.restart_button = RestartButton("Restart", 110, 30, (680, screen_height - 35), BLUE, D_BLUE)
        self.highscore_button = HighscoreButton("Highscores", 110, 30, (680, screen_height - 75), YELLOW, D_YELLOW)

        self.grid_pos = []
        self.set_numpad_pos(680, 40)

        # Enter the coordinates using -> grid_pos[x][y]
        self.text_box = TextBox(110, 30, (self.grid_pos[0][0]), BLACK, WHITE)
        self.button1 = Button("1", 30, 30, (self.grid_pos[0][1]), L_GREY, GREY)
        self.button2 = Button("2", 30, 30, (self.grid_pos[1][1]), L_GREY, GREY)
        self.button3 = Button("3", 30, 30, (self.grid_pos[2][1]), L_GREY, GREY)
        self.button4 = Button("4", 30, 30, (self.grid_pos[0][2]), L_GREY, GREY)
        self.button5 = Button("5", 30, 30, (self.grid_pos[1][2]), L_GREY, GREY)
        self.button6 = Button("6", 30, 30, (self.grid_pos[2][2]), L_GREY, GREY)
        self.button7 = Button("7", 30, 30, (self.grid_pos[0][3]), L_GREY, GREY)
        self.button8 = Button("8", 30, 30, (self.grid_pos[1][3]), L_GREY, GREY)
        self.button9 = Button("9", 30, 30, (self.grid_pos[2][3]), L_GREY, GREY)
        self.button0 = Button("0", 30, 30, (self.grid_pos[1][4]), L_GREY, GREY)
        self.reset_button = ResetButton("X", 30, 30, (self.grid_pos[0][4]), RED, D_RED)
        self.confirm_button = ConfirmButton("C", 30, 30, (self.grid_pos[2][4]), GREEN, D_GREEN)

        # Enter experimental instances here

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        timer.count_up()
        self.draw_ui_rect()
        self.text.draw_text(screen)

        self.draw_numpad()
        self.restart_button.draw(screen)
        self.highscore_button.draw(screen)

        # Enter experimental functions here

    @staticmethod
    def draw_ui_rect():  # this will be replaced with a proper background
        pygame.draw.rect(screen, XL_GREY, (670, 0, 280, 400))  # 'calculator' rect
        pygame.draw.rect(screen, D_RED, (670, 0, 130, 30))  # 'timer' rect
        pygame.draw.rect(screen, L_GREY, (670, 260, 130, 140))  # 'timer' rect
    
    def draw_numpad(self):
        self.text_box.draw(screen)
        self.confirm_button.draw(screen)
        self.reset_button.draw(screen)

        self.button1.draw(screen)
        self.button2.draw(screen)
        self.button3.draw(screen)
        self.button4.draw(screen)
        self.button5.draw(screen)
        self.button6.draw(screen)
        self.button7.draw(screen)
        self.button8.draw(screen)
        self.button9.draw(screen)
        self.button0.draw(screen)

    def set_numpad_pos(self, initial_x, initial_y):
        dynamic_x = initial_x
        dynamic_y = initial_y
        column_count = 3
        row_count = 5
        x_space = 40
        y_space = 45

        # Create a 3d list containing the button grid coordinates
        for x in range(column_count):
            self.grid_pos.append([])
            for y in range(row_count):
                self.grid_pos[x].append([dynamic_x, dynamic_y])
                dynamic_y += y_space
            dynamic_y = initial_y
            dynamic_x += x_space


# Executables -------------------------------------------------------------
if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    screen_width = 800
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    icon = pygame.image.load('number_game.png')

    # Initiate instances
    program = Program()

    # Set caption, icon, color
    pygame.display.set_caption("Number Game!")
    pygame.display.set_icon(icon)

    # Main loop (runs every tick) -------------------------------------------------
    while True:
        # Event code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Game code
        program.run()

        # Updates, mind the order
        pygame.display.flip()
        screen.fill(GREY)

        # Time & Clock
        clock.tick(60)
