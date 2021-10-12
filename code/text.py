import pygame
import timer
import highscore as hs
import globalvar as gv


def normalize_text(text_):
    gv.max_text_length = 10
    text_length = len(text_)
    if text_length < gv.max_text_length:
        for i in range(gv.max_text_length - text_length):
            text_ += " "
        return text_
    else:
        return text_


class TextManager:
    def __init__(self, screen):
        # Initiate instances
        self.clue_text = ClueText(screen)
        # self.timer_text = TimerText()
        # self.highscore_text = HighscoreText()

    def draw(self):
        self.clue_text.draw()


class Text:
    def __init__(self, screen):
        self.screen = screen
        self.text_space = 20
        self.textX = 10  # initial x position
        self.textY = 5  # initial y position
        self.textY_addable = 0
        self.reset_text_y_pos()

    def draw(self, screen):
        self.screen = screen
        # Add text
        self.print_time()

        gv.game_state = gv.game_state
        if gv.game_state == 'main_game' or gv.game_state == 'won' or gv.game_state == 'lost':
            self.clue_text.print_clue_texts()
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

    def print_highscores(self):
        max_highscore = 9
        self.add_line("Highscores!", gv.CREAM)
        highscore = hs.load_hs()
        for index, [player_name, player_time] in enumerate(highscore):
            form_player_time = timer.reformat_time(player_time)
            if index < max_highscore:
                self.add_line(f"#{index + 1}: {player_name}   - Time: {form_player_time}", gv.WHITE)

        highscore_size = len(highscore)
        if highscore_size < max_highscore:
            for i in range(max_highscore - highscore_size):
                self.add_line(f"#{i + highscore_size + 1}: ----------   - Time: --:--", gv.WHITE)

    def set_screen(self, screen):
        self.screen = screen

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


class ClueText(Text):
    def draw(self):
        if gv.game_state == 'main_game' or gv.game_state == 'won' or gv.game_state == 'lost':
            self.print_clue_texts()
        elif gv.game_state == 'won':
            self.input_player_name()

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

        self.check_win_condition()

    def check_win_condition(self):
        if gv.game_state == 'won':
            self.add_line(f"You win! The correct number was {gv.secret_num}", gv.LIME)
        if gv.game_state == 'lost':
            self.add_line(f"You have run out of attempt! You lost. The correct number was {gv.secret_num}", gv.ORANGE)
        if gv.game_state == 'won' or gv.game_state == 'lost':
            self.add_line("Press the restart button to play again", gv.RED)
            timer.stop_timer()

    def input_player_name(self):
        self.add_line(f"Enter your name! (5 letters): {gv.text_input}", gv.ORANGE)


class TimerText(Text):
    pass


class HighscoreText(Text):
    pass

# ---------- Weird and untested stuffs down here ---------- #

"""
class TextCreator:  # Text creator, this is the place to adjust and and text
    def __init__(self):
        self.timer_text = TimerText(680, 5)
        self.clue_text = ClueText(10, 5)
        self.highscore_text = HighscoreText(10, 5)
        # self.num_text_box = TextBox()  # we may have a problem with this one, cause it's part of NumPad

        # timer
        self.timer_text.add_text(f"Timer: {gv.minutes}:{gv.seconds}", gv.WHITE)
        # clue text
        self.clue_text.add_text(f"Guess the 4 digit number combination! You have {gv.remaining_attempts} "
                                f"attempts left", gv.CREAM)

    def update_text(self):  # Runs every frame
        self.timer_text.update_text()
        self.clue_text.update_text()
        self.highscore_text.update_text()

    def draw_text(self, screen):  # Runs every frame
        self.timer_text.draw(screen)
        if gv.game_state == 'main_game' or gv.game_state == 'won' or gv.game_state == 'lost':
            self.clue_text.draw(screen)
        elif gv.game_state == 'highscore':
            self.highscore_text.draw(screen)


class NewText:  # Parent class for Text. Will rename it to Text when stable
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_space = 20
        self.text_data = []  # [text, color]
        # font
        self.chary = pygame.font.Font(gv.chary_font, 20)

    def add_text(self, text, color):
        self.text_data.append([text, color])

    def draw(self, screen):
        for i, (text, color) in enumerate(self.text_data):
            text_obj = self.chary.render(text, True, color)
            screen.blit(text_obj, (self.x, i * self.y_space + self.y))


class ClueText(NewText):
    def update_text(self):  # this code doesn't look right. Also it runs every frame... so
        if gv.is_compared:
            self.add_clue()
            self.check_win_condition()
            self.input_player_name()
            gv.is_compared = False

        if gv.is_restarted:
            self.remove_clues()

    def check_win_condition(self):
        if gv.game_state == 'won':
            self.add_text(f"You win! The correct number was {gv.secret_num}", gv.LIME)
        if gv.game_state == 'lost':
            self.add_text(f"You have run out of attempt! You lost. The correct number was {gv.secret_num}", gv.ORANGE)
        if gv.game_state == 'won' or gv.game_state == 'lost':
            self.add_text("Press the restart button to play again", gv.RED)
            timer.stop_timer()
    
    def add_clue(self):
        i = gv.attempts - 1
        self.text_data.append([f"> Attempt #{gv.attempts}: {gv.correct_num[i]} correct numbers, "
                                   f"{gv.correct_pos[i]} are in the correct position. [{gv.combinations[i]}]", gv.BLUE])

    def remove_clues(self):
        if len(self.text_data) > 1:
            del self.text_data[-1]
        else:
            gv.is_restarted = False

    def input_player_name(self):
        self.add_text(f"Enter your name! (5 letters): {gv.text_input}", gv.ORANGE)


class HighscoreText(NewText):
    def update_text(self):
        max_highscore = 9
        if len(self.text_data) < 1:
            self.add_text("Highscores!", gv.CREAM)
        elif len(self.text_data) < max_highscore:
            highscore = hs.load_hs()
            for index, [player_name, player_time] in enumerate(highscore):
                formatted_player_time = timer.reformat_time(player_time)
                if index < max_highscore:
                    self.add_text(f"#{index + 1}: {player_name}   - Time: {formatted_player_time}", gv.WHITE)

            highscore_size = len(highscore)
            if highscore_size < max_highscore:
                for i in range(max_highscore - highscore_size):
                    self.add_text(f"#{i + highscore_size + 1}: ----------   - Time: --:--", gv.WHITE)


class TimerText(NewText):
    def update_text(self):
        self.text_data[0][0] = f"Timer: {gv.minutes}:{gv.seconds}"
"""
