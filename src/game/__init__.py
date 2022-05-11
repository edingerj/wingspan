from typing import Final

from .display_format import DisplayFormat
from .game_main import GameMain
from .game_main_wrapper import GameMainWrapper
from .info import Info
from .move import Move
from .runtime_flags import RuntimeFlags
from .runtime_flags_wrapper import RuntimeFlagsWrapper
from .turn_phase import TurnPhase

game_instance: Final[GameMainWrapper] = GameMainWrapper()
runtime_flags: Final[RuntimeFlagsWrapper] = RuntimeFlagsWrapper()

__all__ = [
    'DisplayFormat',
    'GameMain',
    'Info',
    'Move',
    'RuntimeFlags',
    'TurnPhase',
    'game_instance',
    'runtime_flags',
]
