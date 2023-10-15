import pygame

import globalvar as gv


def count_up():
    elapsed_time = pygame.time.get_ticks()
    dynamic_time = elapsed_time - gv.static_time
    seconds_ = dynamic_time // 1000 % 60
    minutes_ = dynamic_time // 1000 // 60 % 60
    hours_ = dynamic_time // 1000 // 60 // 60

    if gv.is_timer_running:
        gv.seconds = f"{seconds_:02d}"
        gv.minutes = f"{minutes_:02d}"
        gv.hours = f"{hours_:02d}"
        gv.lapped_time = dynamic_time


def reset_timer():
    start_timer()
    gv.static_time = pygame.time.get_ticks()


def stop_timer():
    gv.is_timer_running = False


def start_timer():
    gv.is_timer_running = True
