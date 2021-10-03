# ----------- Global Variables -----------
# Retro Color
CREAM = (247, 246, 196)
WHITE = (255, 255, 255)
RED = (202, 79, 91)
ORANGE = (241, 157, 93)
GREEN = (43, 89, 80)
LIME = (116, 164, 65)
BLUE = (111, 186, 170)
PURPLE = (45, 22, 45)

# Font
chary_font = 'font/chary___.ttf'

# numbergame variables
correct_num = []
correct_pos = []
combinations = []
attempts = 0
MAX_ATTEMPTS = 8
remaining_attempts = MAX_ATTEMPTS
secret_num = ""
game_state = 'main_game'  # game_state types: 'main_game', 'lost', 'won', 'highscore', 'achievement'

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
