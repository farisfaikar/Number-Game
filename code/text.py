import pygame
import timer
import highscore as hs
import globalvar as gv


def normalize_text(text_):
    max_text_length = 10
    text_length = len(text_)
    if text_length < 5:
        for i in range(max_text_length - text_length):
            text_ += " "
        return text_
    else:
        return text_


class Text:
    def __init__(self):
        self.screen = None
        self.text_space = 20
        self.textX = 10  # initial x position
        self.textY = 5  # initial y position
        self.textY_addable = 0
        self.reset_text_y_pos()

    def draw_text(self, screen):
        self.screen = screen
        # Add text
        self.print_time()
        gv.game_state = gv.game_state
        if gv.game_state == 'main_game' or gv.game_state == 'won' or gv.game_state == 'lost':
            self.print_clue_texts()
        elif gv.game_state == 'highscore':
            self.print_highscores()
        if gv.game_state == 'won':
            self.input_player_name()

        self.reset_text_y_pos()

    def add_line(self, text, color):
        # Hard-coded font
        chary = pygame.font.Font(gv.chary_font, 20)
        # Render text
        line = chary.render(text, True, color)
        self.textY_addable = self.textY_addable + self.text_space
        self.screen.blit(line, (self.textX, self.textY_addable))

    def add_custom_line(self, text, color, x, y):
        # Hard-coded font
        chary = pygame.font.Font(gv.chary_font, 20)
        # Render text
        line = chary.render(text, True, color)
        self.screen.blit(line, (x, y))

    def reset_text_y_pos(self):
        self.textY_addable = self.textY - self.text_space

    def print_time(self):
        self.add_custom_line(f"Timer: {gv.minutes}:{gv.seconds}", gv.WHITE, 680, 5)

    def print_error_message(self):
        if len(gv.error_message) != 0:
            error_message = f"ERROR: {gv.error_message}"
            self.add_custom_line(error_message, gv.RED, 10, 5)
        else:
            self.add_custom_line("", gv.RED, 10, 155)

    def print_clue_texts(self):
        attempts = gv.attempts
        correct_num = gv.correct_num
        correct_pos = gv.correct_pos
        combinations = gv.combinations

        self.add_line(f"Guess the 4 digit number combination! You have {gv.remaining_attempts} "
                      + "attempts left", gv.CREAM)

        for i in range(attempts):
            self.add_line(f"> Attempt #{i + 1}: {correct_num[i]} correct numbers, "
                          f"{correct_pos[i]} are in the correct position. [{combinations[i]}]", gv.BLUE)

        self.print_win_message()

    def print_win_message(self):
        if gv.game_state == 'won':
            self.add_line(f"You win! The correct number was {gv.secret_num}", gv.LIME)
        if gv.game_state == 'lost':
            self.add_line(f"You have run out of attempt! You lost. The correct number was {gv.secret_num}", gv.ORANGE)
        if gv.game_state == 'won' or gv.game_state == 'lost':
            self.add_line("Press the restart button to play again", gv.RED)
            timer.stop_timer()

    def print_highscores(self):
        max_highscore = 9
        self.add_line("Highscores!", gv.CREAM)
        highscore = hs.load_hs()
        for index, [player_name, player_time] in enumerate(highscore):
            form_player_time = timer.reformat_time(player_time)
            self.add_line(f"#{index + 1}: {player_name}          - Time: {form_player_time}", gv.WHITE)

        highscore_size = len(highscore)
        if highscore_size < max_highscore:
            for i in range(max_highscore - highscore_size):
                self.add_line(f"#{i + highscore_size + 1}: ----------   - Time: --:--", gv.WHITE)

    def input_player_name(self):
        self.add_line(f"Enter your name! (5 letters): {gv.text_input}", gv.ORANGE)


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
        chary = pygame.font.Font(gv.chary_font, 20)
        text_surf = chary.render(gv.num_input, True, self.text_color)
        text_rect = text_surf.get_rect(center=rect.center)

        # draw rect
        pygame.draw.rect(screen, self.box_color, rect)
        # draw text
        screen.blit(text_surf, text_rect)
