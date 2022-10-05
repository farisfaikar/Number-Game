import os
import sys
from random import randint

import pygame
from pygame import mixer

import achievement
import globalvar as gv
import highscore as hs
import numbergame
import timer
from button import AchievementButton, HighscoreButton, RestartButton
from numpad import NumPad
from sound import Sound
from text import AchievementText, BootText, ClueText, HighscoreText, TimerText


class BootMenu:
    def __init__(self):
        pygame.mixer.pre_init()
        self.sound = Sound()
        self.sound.play_ambient()
        self.sound.play_boot_up()

        self.boot_text = BootText(10, 5)

    def run(self):
        self.boot_text.draw(screen)


class Game:
    def __init__(self):
        # Enter instances here -----------------------------------------------------
        numbergame.gen_secret_num()

        self.restart_button = RestartButton("Restart", 110, 30, (680, 360), gv.RED)
        self.highscore_button = HighscoreButton(
            "Highscore", 110, 30, (680, 320), gv.BLUE
        )
        self.achievement_button = AchievementButton(
            "Achievement", 110, 30, (680, 280), gv.LIME
        )

        self.numpad = NumPad()

        self.clue_text = ClueText(10, 5)
        self.highscore_text = HighscoreText(10, 5)
        self.achievement_text = AchievementText(10, 5)
        self.timer_text = TimerText(680, 5)

        # Enter experimental instances here

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        timer.count_up()
        self.draw_ui_rect()

        self.numpad.draw(screen)
        self.restart_button.draw(screen)
        self.highscore_button.draw(screen)
        self.achievement_button.draw(screen)

        self.clue_text.draw(screen)
        self.timer_text.draw(screen)
        self.highscore_text.draw(screen)

        self.achievement_text.draw(screen)

        # Enter experimental functions here
        # achv = achievement.load_achievement()
        # print(achv["achv01"])

    @staticmethod
    def draw_ui_rect():
        pygame.draw.rect(screen, gv.CREAM, (670, 0, 280, 400))  # 'numpad' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 0, 130, 30))  # 'timer' rect
        pygame.draw.rect(screen, gv.GREEN, (670, 260, 130, 140))  # 'buttons' rect


class CRT:
    def __init__(self, tv_width, tv_height):
        self.tv_width = tv_width
        self.tv_height = tv_height
        self.tv = pygame.image.load("sprite/tv.png").convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (self.tv_width, self.tv_height))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(self.tv_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, "black", (0, y_pos), (self.tv_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(60, 90))
        self.create_crt_lines()
        screen.blit(self.tv, (0, 0))


# Game Setups -------------------------------------------------------------
# Switch to parent directory
path = os.path.dirname(__file__)
os.chdir(os.path.abspath(os.path.join(path, os.pardir)))
# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
icon = pygame.image.load("sprite/number_game.png")

# Initiate screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set caption, icon, color
pygame.display.set_caption("Number Game!")
pygame.display.set_icon(icon)


def run_boot():
    # Initiate instances
    boot_menu = BootMenu()
    crt = CRT(800, 400)

    # Main loop (runs every tick) -------------------------------------------------
    while True:
        # Event code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                any_key_pressed = mixer.Sound("sound/restart_pressed.wav")
                any_key_pressed.play()
                run_game()

        # Boot code
        boot_menu.run()
        crt.draw()

        # Updates, mind the order
        pygame.display.flip()
        screen.fill(gv.PURPLE)

        # Time & Clock
        clock.tick(60)


def run_game():
    # initialize data.json if it doesn't exist
    hs.check_if_data_exists()

    # Initiate instances
    program = Game()
    crt = CRT(670, 400)

    # Main loop (runs every tick) -------------------------------------------------
    while True:
        # Event code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if gv.game_state == "won":
                    keyboard_pressed = mixer.Sound("sound/keyboard_pressed.wav")
                    backspace_pressed = mixer.Sound("sound/backspace_pressed.wav")
                    enter_pressed = mixer.Sound("sound/confirm_pressed.wav")

                    if event.key == pygame.K_RETURN:
                        enter_pressed.play()
                        gv.game_state = "highscore"
                        hs.save_score()
                    if event.key == pygame.K_BACKSPACE:
                        backspace_pressed.play()
                        gv.text_input = gv.text_input[:-1]
                    else:
                        if len(gv.text_input) < 10:
                            keyboard_pressed.play()
                            gv.text_input += event.unicode

        # Game code
        program.run()
        crt.draw()

        # Updates, mind the order
        pygame.display.flip()
        screen.fill(gv.PURPLE)

        # Time & Clock
        clock.tick(60)


if __name__ == "__main__":
    run_boot()
