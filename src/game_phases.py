import sys
import time

import pygame

from src.components.game_status import GameStatus
from src.components.hand import Hand
from src.components.hand_side import HandSide
from src.components.player import Player
from src.components.scoreboard import Scoreboard
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import update_background_using_scroll, update_press_key, is_close_app_event

GlobalState.load_main_screen()
VisualizationService.load_main_game_displays()

scoreboard = Scoreboard()

P1 = Player()
H1 = Hand(HandSide.RIGHT)
H2 = Hand(HandSide.LEFT)

# Sprite Groups
hands = pygame.sprite.Group()
hands.add(H1)
hands.add(H2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(H1)
all_sprites.add(H2)