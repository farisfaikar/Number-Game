import pygame
import math

# timer variables
static_time = 0
seconds = ""
minutes = ""
hours = ""
lapped_time = 0
is_timer_running = True


def count_up():
    elapsed_time = pygame.time.get_ticks()
    dynamic_time = elapsed_time - static_time
    seconds_ = math.floor(dynamic_time / 1000) % 60
    minutes_ = math.floor(dynamic_time / 1000 / 60) % 60
    hours_ = math.floor(dynamic_time / 1000 / 60 / 60)

    global seconds
    global minutes
    global hours
    global lapped_time

    if is_timer_running:
        seconds = add_0(seconds_)
        minutes = add_0(minutes_)
        hours = add_0(hours_)
        lapped_time = dynamic_time


def reset_timer():
    start_timer()
    global static_time
    static_time = pygame.time.get_ticks()


def add_0(num):
    if len(str(num)) == 1:
        return f"0{num}"
    else:
        return f"{num}"


def stop_timer():
    global is_timer_running
    is_timer_running = False


def start_timer():
    global is_timer_running
    is_timer_running = True


def reformat_time(time):
    seconds_ = math.floor(time / 1000)
    str_seconds = add_0(str(seconds_ % 60))
    str_minutes = add_0(str(math.floor(seconds_ / 60)))
    return f"{str_minutes}:{str_seconds}"
