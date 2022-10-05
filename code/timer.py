import pygame
import globalvar as gv

def count_up():
    elapsed_time = pygame.time.get_ticks()
    dynamic_time = elapsed_time - gv.static_time
    dynamic_time = dynamic_time

    #if one day has elapsed
    if not gv.day_elapsed and dynamic_time>=86400000: 
        gv.test = False
        gv.day_elapsed = True
        gv.num_input ="BRUH"


    seconds_ = dynamic_time // 1000 % 60
    minutes_ = dynamic_time // 1000 // 60 % 60
    hours_ = dynamic_time // 1000 // 60 // 60 % 24

    def add_0(num):
        if len(str(num)) == 1:
            return f"0{num}"
        else:
            return f"{num}"
    
    if gv.is_timer_running:
        gv.seconds = add_0(seconds_)
        gv.minutes = add_0(minutes_)
        gv.hours = add_0(hours_)
        gv.lapped_time = dynamic_time


def reset_timer():
    start_timer()
    gv.static_time = pygame.time.get_ticks()


def stop_timer():
    gv.is_timer_running = False


def start_timer():
    gv.is_timer_running = True
