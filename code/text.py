import pygame
import math
import highscore as hs
import globalvar as gv


class Text:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_space = 20
        self.text_data = []
        # font
        self.chary = pygame.font.Font(gv.chary_font, 20)

    def add_text(self, text, color):
        self.text_data.append([text, color])

    def render(self, screen):
        for i, (text, color) in enumerate(self.text_data):
            text_obj = self.chary.render(text, True, color)
            screen.blit(text_obj, (self.x, i * self.y_space + self.y))

        self.text_data = []


class ClueText(Text):
    def draw(self, screen):
        if gv.game_state == 'won' or gv.game_state == 'lost' or gv.game_state == 'main_game':
            self.add_text(f"Guess the 4 digit number combination! You have {gv.remaining_attempts} "
                          f"attempts left", gv.CREAM)

            for i in range(gv.attempts):
                self.add_text(f"> Attempt #{i + 1}: {gv.correct_num[i]} correct numbers, "
                              f"{gv.correct_pos[i]} are in the correct position. [{gv.combinations[i]}]", gv.BLUE)

        if gv.game_state == 'won':
            self.add_text(f"You win! The correct number was {gv.secret_num}", gv.LIME)
        if gv.game_state == 'lost':
            self.add_text(f"You have run out of attempt! You lost. The correct number was {gv.secret_num}", gv.RED)
        if gv.game_state == 'won' or gv.game_state == 'lost':
            self.add_text("Press the restart button to play again", gv.RED)
            self.add_text(f"Enter your name! (5 letters): {gv.text_input}", gv.ORANGE)

        self.render(screen)


class TimerText(Text):
    def draw(self, screen):
        self.add_text(f"Timer: {gv.minutes}:{gv.seconds}", gv.WHITE)
        self.render(screen)


class HighscoreText(Text):
    def draw(self, screen):
        if gv.game_state == 'highscore':
            max_highscore = 9
            self.add_text("Highscores!", gv.CREAM)

            highscore = hs.load_hs()
            for index, [player_name, player_time] in enumerate(highscore):
                formatted_player_time = self.reformat_time(player_time)
                formatted_player_name = self.reformat_name(player_name)
                if index < max_highscore:
                    self.add_text(f"#{index + 1}: {formatted_player_name} - Time: {formatted_player_time}", gv.WHITE)

            if len(highscore) < max_highscore:
                for i in range(max_highscore - len(highscore)):
                    dashes = "-" * gv.max_text_length
                    self.add_text(f"#{i + len(highscore) + 1}: {dashes} - Time: --:--", gv.WHITE)

        self.render(screen)

    @staticmethod
    def reformat_name(name):
        gv.max_text_length = 10
        text_length = len(name)
        if text_length < gv.max_text_length:
            for i in range(gv.max_text_length - text_length):
                name += " "
            return name
        else:
            return name

    @staticmethod
    def reformat_time(time):
        def add_0(num):
            if len(str(num)) == 1:
                return f"0{num}"
            else:
                return f"{num}"

        seconds = math.floor(time / 1000)
        str_seconds = add_0(str(seconds % 60))
        str_minutes = add_0(str(math.floor(seconds / 60)))
        return f"{str_minutes}:{str_seconds}"
