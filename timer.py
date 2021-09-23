import pygame
import math
import numbergame

static_time = 0
seconds = ""
minutes = ""
hours = ""


def count_up():
    elapsed_time = pygame.time.get_ticks()
    dynamic_time = elapsed_time - static_time
    seconds_ = math.floor(dynamic_time / 1000) % 60
    minutes_ = math.floor(dynamic_time / 1000 / 60) % 60
    hours_ = math.floor(dynamic_time / 1000 / 60 / 60)

    global seconds
    global minutes
    global hours

    if not numbergame.is_win and not numbergame.is_lost:
        seconds = add_0(seconds_)
        minutes = add_0(minutes_)
        hours = add_0(hours_)


def reset_timer():
    global static_time
    static_time = pygame.time.get_ticks()


def add_0(num):
    if len(str(num)) == 1:
        return f"0{num}"
    else:
        return f"{num}"
