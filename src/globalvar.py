# ----------- Global Variables -----------
# Retro Color
CREAM = (247, 246, 196)  # hex : #f7f4c4
WHITE = (255, 255, 255)
RED = (202, 79, 91)  # hex : #ca4f7c
ORANGE = (241, 157, 93)  # hex : #f19d5d
GREEN = (43, 89, 80)
LIME = (116, 164, 65)  # hex : #74a441
BLUE = (111, 186, 170)
PURPLE = (45, 22, 45)  # hex: #2d162d

# Font
chary_font = "font/chary___.ttf"

# numbergame variables
MAX_ATTEMPTS = 8
remaining_attempts = MAX_ATTEMPTS
correct_num = []
correct_pos = []
combinations = []
attempts = 0
secret_num = ""
game_state = "main_game"  # game_state identifiers: 'main_game', 'lost', 'won', 'highscore', 'achievement'

# button variables
num_input = ""
error_message = ""

# timer variables
static_time = 0
seconds = ""
minutes = ""
hours = ""
lapped_time = 0
is_timer_running = True

# text variables
text_input = ""
MAX_TEXT_LENGTH = 10
MAX_HIGHSCORE_LIST = 9


ACHIEVEMENT_LIST = [
    "I did it!: Finish the puzzle for the first time",
    "Quick Solver: Finish the puzzle in less than 1 minute",
    "Speedrunner: Finish the puzzle in less than 10 seconds",
    "The Dragon: Solve the puzzle in one attempt",
    "Sloth: Finish the puzzle in more than an hour",
    "AFK: Leave the game running for a day",
]
