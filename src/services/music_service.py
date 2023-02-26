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

    @staticmethod
    def get_chop_musics():
        return [
            AUDIO_DIR / "chop.wav",
            AUDIO_DIR / "chop_2.wav",
            AUDIO_DIR / "chop_3.wav"
        ]

    @staticmethod
    def get_cheer_musics():
        return [
            AUDIO_DIR / "cheer.wav",
            AUDIO_DIR / "cheer_2.wav",
            AUDIO_DIR / "cheer_3.wav",
            AUDIO_DIR / "cheer_4.wav"
        ]