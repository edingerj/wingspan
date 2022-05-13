from enum import Enum

from util.ansi import AnsiColor


class PlayerColor(Enum):
    RED = 'RED'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    BLUE = 'BLUE'
    MAGENTA = 'MAGENTA'

    def ansi(self: 'PlayerColor') -> AnsiColor:
        if self is PlayerColor.RED:
            return AnsiColor.RED
        elif self is PlayerColor.YELLOW:
            return AnsiColor.YELLOW
        elif self is PlayerColor.GREEN:
            return AnsiColor.GREEN
        elif self is PlayerColor.BLUE:
            return AnsiColor.BLUE
        elif self is PlayerColor.MAGENTA:
            return AnsiColor.MAGENTA

    def table_format(self: 'PlayerColor') -> str:
        return self.ansi().foreground(self.value.lower())
