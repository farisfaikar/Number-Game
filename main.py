import pygame, sys
import text
from button import Button, ConfirmButton, ResetButton

# Global RGB (this shouldn't be here, idk where to put it though)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
L_GREY = (100, 100, 100)
D_GREY = (25, 25, 25)
WHITE = (255, 255, 255)
BLUE = (150, 150, 255)
D_BLUE = (100, 100, 200)
CYAN = (150, 255, 255)
GREEN = (150, 255, 150)
D_GREEN = (100, 200, 100)
RED = (255, 150, 150)
D_RED = (200, 100, 100)
YELLOW = (255, 255, 150)
PURPLE = (255, 0, 255)


class Program:
    def __init__(self):
        # Enter instances here -----------------------------------------------------
        self.rect = text.Rect()
        self.text = text.Text()

        # Enter beta version instances here
        self.confirm_button = ConfirmButton("C", 30, 30, (680, 335), GREEN, D_GREEN)
        self.reset_button = ResetButton("X", 30, 30, (600, 335), RED, D_RED)

        self.button1 = Button("1", 30, 30, (600, 200), L_GREY, GREY)
        self.button2 = Button("2", 30, 30, (640, 200), L_GREY, GREY)
        self.button3 = Button("3", 30, 30, (680, 200), L_GREY, GREY)
        self.button4 = Button("4", 30, 30, (600, 245), L_GREY, GREY)
        self.button5 = Button("5", 30, 30, (640, 245), L_GREY, GREY)
        self.button6 = Button("6", 30, 30, (680, 245), L_GREY, GREY)
        self.button7 = Button("7", 30, 30, (600, 290), L_GREY, GREY)
        self.button8 = Button("8", 30, 30, (640, 290), L_GREY, GREY)
        self.button9 = Button("9", 30, 30, (680, 290), L_GREY, GREY)
        self.button0 = Button("0", 30, 30, (640, 335), L_GREY, GREY)

        self.text_box = text.TextBox(110, 30, (600, 155), BLACK, WHITE)

        # Enter experimental instances here

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        self.rect.draw_ui_rect(screen)
        self.text.draw_text(screen)

        # Enter beta version functions here
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

        self.text_box.draw(screen)

        # Enter experimental functions here


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
    pygame.display.set_caption("Better Formatting: Number Game!")
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
