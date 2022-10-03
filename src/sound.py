import random

from pygame import mixer


class Sound:
    def __init__(self):
        boot_up_sound = [
            "sound/boot_up.ogg",
            "sound/tator_boot_up.ogg",
            "sound/malf_boot_up.ogg",
            "sound/ops_boot_up.ogg",
        ]

        rnd_int = random.randint(1, 100)
        if 0 < rnd_int < 99:
            random_boot_up = boot_up_sound[0]
        else:
            random_boot_up = boot_up_sound[random.randint(1, len(boot_up_sound) - 1)]

        mixer.music.load("sound/server_ambient.ogg")
        mixer.music.set_volume(0.5)
        self.boot_up = mixer.Sound(random_boot_up)
        self.boot_up.set_volume(0.7)

    @staticmethod
    def play_ambient():
        mixer.music.play(-1)

    def play_boot_up(self):
        self.boot_up.play()
