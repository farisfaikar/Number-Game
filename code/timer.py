import pygame
import math
import globalvar as gv


def count_up():
    elapsed_time = pygame.time.get_ticks()
    dynamic_time = elapsed_time - gv.static_time
    seconds_ = math.floor(dynamic_time / 1000) % 60
    minutes_ = math.floor(dynamic_time / 1000 / 60) % 60
    hours_ = math.floor(dynamic_time / 1000 / 60 / 60)

    if gv.is_timer_running:
        gv.seconds = add_0(seconds_)
        gv.minutes = add_0(minutes_)
        gv.hours = add_0(hours_)
        gv.lapped_time = dynamic_time


def reset_timer():
    start_timer()
    gv.static_time = pygame.time.get_ticks()


def add_0(num):
    if len(str(num)) == 1:
        return f"0{num}"
    else:
        return f"{num}"


def stop_timer():
    gv.is_timer_running = False


def start_timer():
    gv.is_timer_running = True
