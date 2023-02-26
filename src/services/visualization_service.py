import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine

class VisualizationService:
    @staticmethod
    def get_right_hand_image():
        return pygame.image.load(ASSETS_DIR / "right_hand.png").convert_alpha()

    @staticmethod
    def get_left_hand_image():
        return pygame.image.load(ASSETS_DIR / "left_hand.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "gift.png").convert_alpha()

    @staticmethod
    def get_dotted_line():
        return pygame.image.load(ASSETS_DIR / "dotted_line.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_santa_hand():
        return pygame.image.load(ASSETS_DIR / "santa_hand.png").convert_alpha()

    @staticmethod
    def get_score_backing():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_key.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title.png").convert_alpha()

    @staticmethod
    def get_holding_gift_image():
        return pygame.image.load(MENU_DIR / "holding_gift.png").convert_alpha()