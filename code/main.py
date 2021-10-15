import pygame
import sys

from random import randint
<<<<<<< HEAD
from text import Text, TextBox, TextManager
from button import Button, ConfirmButton, ResetButton, RestartButton, HighscoreButton, AchievementButton
import text
=======
from numpad import NumPad
from button import RestartButton, HighscoreButton, AchievementButton
from text import ClueText, TimerText, HighscoreText
>>>>>>> 060f11eaa8cf6a54be7a01d37d284effd0923d3f
import numbergame
import timer
import highscore as hs
import globalvar as gv


class Program:
    def __init__(self):
        # Enter instances here -----------------------------------------------------
        numbergame.gen_secret_num()

        self.restart_button = RestartButton("Restart", 110, 30, (680, screen_height - 40), gv.RED)
        self.highscore_button = HighscoreButton("Highscore", 110, 30, (680, screen_height - 80), gv.BLUE)
        self.achievement_button = AchievementButton("Achievement", 110, 30, (680, screen_height - 120), gv.LIME)

<<<<<<< HEAD
        self.grid_pos = []
        self.set_numpad_pos(680, 40)

        # Enter the coordinates using -> grid_pos[x][y]
        self.text_box = TextBox(110, 30, (self.grid_pos[0][0]), gv.PURPLE, gv.WHITE)
        self.button1 = Button("1", 30, 30, (self.grid_pos[0][1]), gv.ORANGE)
        self.button2 = Button("2", 30, 30, (self.grid_pos[1][1]), gv.ORANGE)
        self.button3 = Button("3", 30, 30, (self.grid_pos[2][1]), gv.ORANGE)
        self.button4 = Button("4", 30, 30, (self.grid_pos[0][2]), gv.ORANGE)
        self.button5 = Button("5", 30, 30, (self.grid_pos[1][2]), gv.ORANGE)
        self.button6 = Button("6", 30, 30, (self.grid_pos[2][2]), gv.ORANGE)
        self.button7 = Button("7", 30, 30, (self.grid_pos[0][3]), gv.ORANGE)
        self.button8 = Button("8", 30, 30, (self.grid_pos[1][3]), gv.ORANGE)
        self.button9 = Button("9", 30, 30, (self.grid_pos[2][3]), gv.ORANGE)
        self.button0 = Button("0", 30, 30, (self.grid_pos[1][4]), gv.ORANGE)
        self.reset_button = ResetButton("X", 30, 30, (self.grid_pos[0][4]), gv.RED)
        self.confirm_button = ConfirmButton("=", 30, 30, (self.grid_pos[2][4]), gv.LIME)
=======
        self.numpad = NumPad()

        self.clue_text = ClueText(10, 5, screen)
        self.timer_text = TimerText(680, 5, screen)
        self.highscore_text = HighscoreText(10, 5, screen)
>>>>>>> 060f11eaa8cf6a54be7a01d37d284effd0923d3f

        # Enter experimental instances here
        # self.text_creator = text.TextCreator()
        self.text_manager = TextManager(screen)

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        timer.count_up()
        self.draw_ui_rect()
<<<<<<< HEAD
        # self.text.draw_text(screen)
=======
>>>>>>> 060f11eaa8cf6a54be7a01d37d284effd0923d3f

        self.numpad.draw(screen)
        self.restart_button.draw(screen)
        self.highscore_button.draw(screen)
        self.achievement_button.draw(screen)

        self.clue_text.draw()
        self.timer_text.draw()
        self.highscore_text.draw()

        # Enter experimental functions here
        # self.text_creator.update_text()
        # self.text_creator.draw_text(screen)
        self.text_manager.draw()

    @staticmethod
    def draw_ui_rect():
        pygame.draw.rect(screen, gv.CREAM, (670, 0, 280, 400))  # 'calculator' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 0, 130, 30))  # 'timer' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 260, 130, 140))  # 'timer' rect
<<<<<<< HEAD
    
    def draw_numpad(self):  #TODO seperate this to a different module
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
        column_count = 3
        row_count = 5
        x_space = 40
        y_space = 45

        # Create a 3d list containing the button grid coordinates
        for x in range(column_count):
            self.grid_pos.append([])
            for y in range(row_count):
                self.grid_pos[x].append([x * x_space + initial_x, y * y_space + initial_y])
=======
>>>>>>> 060f11eaa8cf6a54be7a01d37d284effd0923d3f


class CRT:
    def __init__(self):
        self.tv_width = 670
        self.tv = pygame.image.load('sprites/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (self.tv_width, screen_height))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(screen_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (self.tv_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(60, 90))
        self.create_crt_lines()
        screen.blit(self.tv, (0, 0))


# Executables -------------------------------------------------------------
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))


def main():
    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    icon = pygame.image.load('sprites/number_game.png')

    # Initiate instances
    program = Program()
    crt = CRT()

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
            if event.type == pygame.KEYDOWN:
                if gv.game_state == 'won':
                    if event.key == pygame.K_RETURN:
                        gv.game_state = 'highscore'
                        hs.save_score()
                    if event.key == pygame.K_BACKSPACE:
                        gv.text_input = gv.text_input[:-1]
                    else:
                        if len(gv.text_input) < 10:
                            gv.text_input += event.unicode

        # Game code
        program.run()
        crt.draw()

        # Updates, mind the order
        pygame.display.flip()
        screen.fill(gv.PURPLE)

        # Time & Clock
        clock.tick(60)


if __name__ == '__main__':
    main()
