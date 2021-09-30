import pygame
import math
import time


class Timer:
    def count_up(self):
        ticking = True
        seconds = 0
        minutes = 0
        while ticking:
            for sec in range(seconds, 59):
                seconds += 1
                time.sleep(1)
                print(f"Timer: {minutes}:{seconds}")
            minutes += 1
            seconds = 0


class TestTimer:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0
        self.ticked = False

    def count_up(self):
        miliseconds = pygame.time.get_ticks()
        seconds_elapsed = math.floor(miliseconds / 1000)
        self.seconds = seconds_elapsed - (self.minutes * 10)
        seconds_ = seconds_elapsed % 10
        print(seconds_)
        if seconds_elapsed % 10 == 0 and not self.ticked:
            self.minutes += 1
            self.ticked = True

        # print(f"Seconds elapsed: {seconds_elapsed}")
        # print(f"Timer: {self.minutes}:{self.seconds}")
