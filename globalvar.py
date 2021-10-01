# ----------- Global Variables -----------
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
