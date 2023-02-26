import random

import pygame

from paths import AUDIO_DIR

class MusicService:
    @staticmethod
    def get_background_musics():
        return [
            AUDIO_DIR / "sleigh_ride.ogg",
            AUDIO_DIR / "merry_christmas.ogg",
            AUDIO_DIR / "here_comes_santa.ogg"
        ]