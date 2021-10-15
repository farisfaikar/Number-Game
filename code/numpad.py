import pygame
import globalvar as gv
from button import Button, ConfirmButton, ResetButton


class NumDisplay:
    def __init__(self, width, height, pos, box_color, text_color):
        self.width = width
        self.height = height
        self.pos = pos
        self.box_color = box_color
        self.text_color = text_color

    def draw(self, screen):
        # create textbox
        rect = pygame.Rect(self.pos, (self.width, self.height))
        chary = pygame.font.Font(gv.chary_font, 20)
        text_surf = chary.render(gv.num_input, True, self.text_color)
        text_rect = text_surf.get_rect(center=rect.center)

        # draw rect
        pygame.draw.rect(screen, self.box_color, rect)
        # draw text
        screen.blit(text_surf, text_rect)


class NumPad:
    def __init__(self):
        self.grid_pos = []
        self.set_numpad_pos(680, 40)

        # Enter the coordinates using -> grid_pos[x][y]
        self.text_box = NumDisplay(110, 30, (self.grid_pos[0][0]), gv.PURPLE, gv.WHITE)
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

    def draw(self, screen):
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
