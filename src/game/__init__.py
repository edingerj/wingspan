from typing import Final

from .game_main import GameMain
from .game_main_wrapper import GameMainWrapper
from .game_results import GameResults
from .move import Move

game_instance: Final[GameMainWrapper] = GameMainWrapper()

__all__ = [
    'GameMain',
    'GameResults',
    'game_instance',
    'Move',
]
