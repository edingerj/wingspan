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
            return AnsiFormat.fg_black(text)
        elif self is AnsiColor.RED:
            return AnsiFormat.fg_red(text)
        elif self is AnsiColor.GREEN:
            return AnsiFormat.fg_green(text)
        elif self is AnsiColor.YELLOW:
            return AnsiFormat.fg_yellow(text)
        elif self is AnsiColor.BLUE:
            return AnsiFormat.fg_blue(text)
        elif self is AnsiColor.MAGENTA:
            return AnsiFormat.fg_magenta(text)
        elif self is AnsiColor.CYAN:
            return AnsiFormat.fg_cyan(text)
        elif self is AnsiColor.WHITE:
            return AnsiFormat.fg_white(text)
        elif self is AnsiColor.BRIGHT_BLACK:
            return AnsiFormat.fg_bright_black(text)
        elif self is AnsiColor.BRIGHT_RED:
            return AnsiFormat.fg_bright_red(text)
        elif self is AnsiColor.BRIGHT_GREEN:
            return AnsiFormat.fg_bright_green(text)
        elif self is AnsiColor.BRIGHT_YELLOW:
            return AnsiFormat.fg_bright_yellow(text)
        elif self is AnsiColor.BRIGHT_BLUE:
            return AnsiFormat.fg_bright_blue(text)
        elif self is AnsiColor.BRIGHT_MAGENTA:
            return AnsiFormat.fg_bright_magenta(text)
        elif self is AnsiColor.BRIGHT_CYAN:
            return AnsiFormat.fg_bright_cyan(text)
        elif self is AnsiColor.BRIGHT_WHITE:
            return AnsiFormat.fg_bright_white(text)

    def background(self: 'AnsiColor', text: str) -> str:
        if self is AnsiColor.DEFAULT:
            return text
        elif self is AnsiColor.BLACK:
            return AnsiFormat.bg_black(text)
        elif self is AnsiColor.RED:
            return AnsiFormat.bg_red(text)
        elif self is AnsiColor.GREEN:
            return AnsiFormat.bg_green(text)
        elif self is AnsiColor.YELLOW:
            return AnsiFormat.bg_yellow(text)
        elif self is AnsiColor.BLUE:
            return AnsiFormat.bg_blue(text)
        elif self is AnsiColor.MAGENTA:
            return AnsiFormat.bg_magenta(text)
        elif self is AnsiColor.CYAN:
            return AnsiFormat.bg_cyan(text)
        elif self is AnsiColor.WHITE:
            return AnsiFormat.bg_white(text)
        elif self is AnsiColor.BRIGHT_BLACK:
            return AnsiFormat.bg_bright_black(text)
        elif self is AnsiColor.BRIGHT_RED:
            return AnsiFormat.bg_bright_red(text)
        elif self is AnsiColor.BRIGHT_GREEN:
            return AnsiFormat.bg_bright_green(text)
        elif self is AnsiColor.BRIGHT_YELLOW:
            return AnsiFormat.bg_bright_yellow(text)
        elif self is AnsiColor.BRIGHT_BLUE:
            return AnsiFormat.bg_bright_blue(text)
        elif self is AnsiColor.BRIGHT_MAGENTA:
            return AnsiFormat.bg_bright_magenta(text)
        elif self is AnsiColor.BRIGHT_CYAN:
            return AnsiFormat.bg_bright_cyan(text)
        elif self is AnsiColor.BRIGHT_WHITE:
            return AnsiFormat.bg_bright_white(text)
