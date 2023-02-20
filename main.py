import pygame

from src.components.game_status import GameStatus
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService

pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)