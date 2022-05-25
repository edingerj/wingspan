from typing import Final

from gameplay.base import GameMainWrapper
from gameplay.base.runtime import RuntimeFlagsWrapper

game_instance: Final[GameMainWrapper] = GameMainWrapper()
runtime_flags: Final[RuntimeFlagsWrapper] = RuntimeFlagsWrapper()

__all__ = [
    'game_instance',
    'runtime_flags',
]
