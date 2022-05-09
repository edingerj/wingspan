from typing import Final

from .display_format import DisplayFormat
from .game_main import GameMain
from .game_main_wrapper import GameMainWrapper
from .move import Move
from .runtime_flags import RuntimeFlags
from .runtime_flags_wrapper import RuntimeFlagsWrapper

game_instance: Final[GameMainWrapper] = GameMainWrapper()
runtime_flags: Final[RuntimeFlagsWrapper] = RuntimeFlagsWrapper()

__all__ = [
    'DisplayFormat',
    'GameMain',
    'Move',
    'RuntimeFlags',
    'game_instance',
    'runtime_flags',
]
