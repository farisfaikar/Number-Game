import pygame, sys
import text
from button import Button, ConfirmButton, ResetButton, RestartButton

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

        self.restart_button = RestartButton("R", 30, 30, (10, 10), BLUE, D_BLUE)

        self.set_numpad_pos(0, 0)

        self.button1 = Button("1", 30, 30, (680, 215), L_GREY, GREY)
        self.button2 = Button("2", 30, 30, (720, 215), L_GREY, GREY)
        self.button3 = Button("3", 30, 30, (760, 215), L_GREY, GREY)
        self.button4 = Button("4", 30, 30, (680, 260), L_GREY, GREY)
        self.button5 = Button("5", 30, 30, (720, 260), L_GREY, GREY)
        self.button6 = Button("6", 30, 30, (760, 260), L_GREY, GREY)
        self.button7 = Button("7", 30, 30, (680, 305), L_GREY, GREY)
        self.button8 = Button("8", 30, 30, (720, 305), L_GREY, GREY)
        self.button9 = Button("9", 30, 30, (760, 305), L_GREY, GREY)
        self.button0 = Button("0", 30, 30, (720, 350), L_GREY, GREY)
        self.reset_button = ResetButton("X", 30, 30, (680, 350), RED, D_RED)
        self.confirm_button = ConfirmButton("C", 30, 30, (760, 350), GREEN, D_GREEN)

        self.text_box = text.TextBox(110, 30, (600, 155), BLACK, WHITE)

        # Enter experimental instances here

    def run(self):  # This bad boy runs every frame -------------------------------
        # Enter functions here
        self.rect.draw_ui_rect(screen)
        self.text.draw_text(screen)

        self.draw_numpad(screen)

        self.restart_button.draw(screen)
        

        # Enter experimental functions here
    
    def draw_numpad(self, screen):
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
        grid_x = []
        grid_y = []
        grid_x.append(initial_x)
        grid_y.append(initial_y)
        dynamic_x = initial_x
        dynamic_y = initial_y
        column_count = 3
        row_count = 5
        x_space = 40
        y_space = 45

        for x in range(column_count - 1):
            grid_x.append(dynamic_x + x_space)
            dynamic_x += x_space
        for y in range(row_count - 1):
            grid_y.append(dynamic_y + y_space)
            dynamic_y += y_space

        print(f"grid_x: {grid_x}")
        print(f"grid_y: {grid_y}")


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
