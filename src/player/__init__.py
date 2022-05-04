from typing import Final, List

from .arboretum import Arboretum
from .player import Player

all_players: Final[List[Player]] = []
computer: Final[Player] = Player()

__all__ = [
    Arboretum,
    Player,
    all_players,
    computer,
]
