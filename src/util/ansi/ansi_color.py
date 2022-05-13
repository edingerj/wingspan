from enum import Enum

from util.ansi.ansi_format import AnsiFormat


class AnsiColor(Enum):
    DEFAULT = 'DEFAULT'
    BLACK = 'BLACK'
    RED = 'RED'
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    BLUE = 'BLUE'
    MAGENTA = 'MAGENTA'
    CYAN = 'CYAN'
    WHITE = 'WHITE'
    BRIGHT_BLACK = 'BRIGHT_BLACK'
    BRIGHT_RED = 'BRIGHT_RED'
    BRIGHT_GREEN = 'BRIGHT_GREEN'
    BRIGHT_YELLOW = 'BRIGHT_YELLOW'
    BRIGHT_BLUE = 'BRIGHT_BLUE'
    BRIGHT_MAGENTA = 'BRIGHT_MAGENTA'
    BRIGHT_CYAN = 'BRIGHT_CYAN'
    BRIGHT_WHITE = 'BRIGHT_WHITE'

    def foreground(self: 'AnsiColor', text: str) -> str:
        if self is AnsiColor.DEFAULT:
            return text
        elif self is AnsiColor.BLACK:
            return AnsiFormat.black(text)
        elif self is AnsiColor.RED:
            return AnsiFormat.red(text)
        elif self is AnsiColor.GREEN:
            return AnsiFormat.green(text)
        elif self is AnsiColor.YELLOW:
            return AnsiFormat.yellow(text)
        elif self is AnsiColor.BLUE:
            return AnsiFormat.blue(text)
        elif self is AnsiColor.MAGENTA:
            return AnsiFormat.magenta(text)
        elif self is AnsiColor.CYAN:
            return AnsiFormat.cyan(text)
        elif self is AnsiColor.WHITE:
            return AnsiFormat.white(text)
        elif self is AnsiColor.BRIGHT_BLACK:
            return AnsiFormat.bright_black(text)
        elif self is AnsiColor.BRIGHT_RED:
            return AnsiFormat.bright_red(text)
        elif self is AnsiColor.BRIGHT_GREEN:
            return AnsiFormat.bright_green(text)
        elif self is AnsiColor.BRIGHT_YELLOW:
            return AnsiFormat.bright_yellow(text)
        elif self is AnsiColor.BRIGHT_BLUE:
            return AnsiFormat.bright_blue(text)
        elif self is AnsiColor.BRIGHT_MAGENTA:
            return AnsiFormat.bright_magenta(text)
        elif self is AnsiColor.BRIGHT_CYAN:
            return AnsiFormat.bright_cyan(text)
        elif self is AnsiColor.BRIGHT_WHITE:
            return AnsiFormat.bright_white(text)
