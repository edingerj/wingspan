from typing import Final

from .game_loop import GameLoop
from .move import Move

game_instance: Final[GameLoop] = GameLoop()

__all__ = [
    GameLoop,
    game_instance,
    Move,
]
