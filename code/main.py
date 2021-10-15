import pygame
import sys

from random import randint
from numpad import NumPad
from button import RestartButton, HighscoreButton, AchievementButton
from text import ClueText, TimerText, HighscoreText
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

        self.numpad = NumPad()

        self.clue_text = ClueText(10, 5, screen)
        self.timer_text = TimerText(680, 5, screen)
        self.highscore_text = HighscoreText(10, 5, screen)

        # Enter experimental instances here

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        timer.count_up()
        self.draw_ui_rect()

        self.numpad.draw(screen)
        self.restart_button.draw(screen)
        self.highscore_button.draw(screen)
        self.achievement_button.draw(screen)

        self.clue_text.draw()
        self.timer_text.draw()
        self.highscore_text.draw()

        # Enter experimental functions here

    @staticmethod
    def draw_ui_rect():
        pygame.draw.rect(screen, gv.CREAM, (670, 0, 280, 400))  # 'calculator' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 0, 130, 30))  # 'timer' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 260, 130, 140))  # 'timer' rect


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
