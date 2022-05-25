from abc import ABC
from typing import List

from gameplay.base.runtime import RuntimeFlags, DisplayFormat


class ConsoleRuntimeFlags(RuntimeFlags, ABC):
    def __init__(
            self: 'ConsoleRuntimeFlags',
            experimental=True,
            no_sleep=False,
    ):
        super(ConsoleRuntimeFlags, self).__init__(
            display_format=DisplayFormat.CONSOLE,
            experimental=experimental,
        )
        self.no_sleep = no_sleep

    @staticmethod
    def from_arguments(arguments: List[str]) -> 'ConsoleRuntimeFlags':
        return ConsoleRuntimeFlags(
            experimental='--experimental' in arguments,
            no_sleep='--no-sleep' in arguments,
        )
