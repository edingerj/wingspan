from re import compile
from typing import Final

from util.ansi.escape_characters import *


class AnsiFormat:
    """
    Accounts for the length of added ANSI escape characters
    when using length formatting utilities like str.ljust()
    """
    ATTR_LEN_OFFSET: Final[int] = 9
    COLOR_LEN_OFFSET: Final[int] = 10

    @staticmethod
    def unformat(text: str) -> str:
        ansi_escape = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    # region Text Attributes
    @staticmethod
    def bold(text: str) -> str:
        return '{}{}{}'.format(BOLD, text, WEIGHT_OFF)

    @staticmethod
    def faint(text: str) -> str:
        return '{}{}{}'.format(FAINT, text, WEIGHT_OFF)

    @staticmethod
    def italic(text: str) -> str:
        return '{}{}{}'.format(ITALIC, text, ITALIC_OFF)

    @staticmethod
    def underscore(text: str) -> str:
        return '{}{}{}'.format(UNDERSCORE, text, UNDERSCORE_OFF)

    @staticmethod
    def blink(text: str) -> str:
        return '{}{}{}'.format(BLINK, text, BLINK_OFF)

    @staticmethod
    def invert(text: str) -> str:
        return '{}{}{}'.format(INVERT, text, INVERT_OFF)

    @staticmethod
    def conceal(text: str) -> str:
        return '{}{}{}'.format(CONCEAL, text, CONCEAL_OFF)

    @staticmethod
    def strikethrough(text: str) -> str:
        return '{}{}{}'.format(STRIKETHROUGH, text, STRIKETHROUGH_OFF)
    # endregion Text Attributes

    # region Foreground Colors
    @staticmethod
    def fg_black(text: str) -> str:
        return '{}{}{}'.format(FG_BLACK, text, FG_OFF)

    @staticmethod
    def fg_red(text: str) -> str:
        return '{}{}{}'.format(FG_RED, text, FG_OFF)

    @staticmethod
    def fg_green(text: str) -> str:
        return '{}{}{}'.format(FG_GREEN, text, FG_OFF)

    @staticmethod
    def fg_yellow(text: str) -> str:
        return '{}{}{}'.format(FG_YELLOW, text, FG_OFF)

    @staticmethod
    def fg_blue(text: str) -> str:
        return '{}{}{}'.format(FG_BLUE, text, FG_OFF)

    @staticmethod
    def fg_magenta(text: str) -> str:
        return '{}{}{}'.format(FG_MAGENTA, text, FG_OFF)

    @staticmethod
    def fg_cyan(text: str) -> str:
        return '{}{}{}'.format(FG_CYAN, text, FG_OFF)

    @staticmethod
    def fg_white(text: str) -> str:
        return '{}{}{}'.format(FG_WHITE, text, FG_OFF)
    # endregion Foreground Colors

    # region Background Colors
    @staticmethod
    def bg_black(text: str) -> str:
        return '{}{}{}'.format(BG_BLACK, text, BG_OFF)

    @staticmethod
    def bg_red(text: str) -> str:
        return '{}{}{}'.format(BG_RED, text, BG_OFF)

    @staticmethod
    def bg_green(text: str) -> str:
        return '{}{}{}'.format(BG_GREEN, text, BG_OFF)

    @staticmethod
    def bg_yellow(text: str) -> str:
        return '{}{}{}'.format(BG_YELLOW, text, BG_OFF)

    @staticmethod
    def bg_blue(text: str) -> str:
        return '{}{}{}'.format(BG_BLUE, text, BG_OFF)

    @staticmethod
    def bg_magenta(text: str) -> str:
        return '{}{}{}'.format(BG_MAGENTA, text, BG_OFF)

    @staticmethod
    def bg_cyan(text: str) -> str:
        return '{}{}{}'.format(BG_CYAN, text, BG_OFF)

    @staticmethod
    def bg_white(text: str) -> str:
        return '{}{}{}'.format(BG_WHITE, text, BG_OFF)
    # endregion Background Colors

    # region Bright Foreground Colors
    @staticmethod
    def fg_bright_black(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_BLACK, text, FG_OFF)

    @staticmethod
    def fg_bright_red(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_RED, text, FG_OFF)

    @staticmethod
    def fg_bright_green(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_GREEN, text, FG_OFF)

    @staticmethod
    def fg_bright_yellow(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_YELLOW, text, FG_OFF)

    @staticmethod
    def fg_bright_blue(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_BLUE, text, FG_OFF)

    @staticmethod
    def fg_bright_magenta(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_MAGENTA, text, FG_OFF)

    @staticmethod
    def fg_bright_cyan(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_CYAN, text, FG_OFF)

    @staticmethod
    def fg_bright_white(text: str) -> str:
        return '{}{}{}'.format(FG_BRIGHT_WHITE, text, FG_OFF)
    # endregion Bright Foreground Colors

    # region Bright Background Colors
    @staticmethod
    def bg_bright_black(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_BLACK, text, BG_OFF)

    @staticmethod
    def bg_bright_red(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_RED, text, BG_OFF)

    @staticmethod
    def bg_bright_green(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_GREEN, text, BG_OFF)

    @staticmethod
    def bg_bright_yellow(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_YELLOW, text, BG_OFF)

    @staticmethod
    def bg_bright_blue(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_BLUE, text, BG_OFF)

    @staticmethod
    def bg_bright_magenta(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_MAGENTA, text, BG_OFF)

    @staticmethod
    def bg_bright_cyan(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_CYAN, text, BG_OFF)

    @staticmethod
    def bg_bright_white(text: str) -> str:
        return '{}{}{}'.format(BG_BRIGHT_WHITE, text, BG_OFF)
    # endregion Bright Background Colors


if __name__ == '__main__':
    print('\nText Attributes:')
    print('bold: ' + AnsiFormat.bold('01189998819991197253'))
    print('faint: ' + AnsiFormat.faint('01189998819991197253'))
    print('italic: ' + AnsiFormat.italic('01189998819991197253'))
    print('underscore: ' + AnsiFormat.underscore('01189998819991197253'))
    print('blink: ' + AnsiFormat.blink('01189998819991197253'))
    print('invert: ' + AnsiFormat.invert('01189998819991197253'))
    print('conceal: ' + AnsiFormat.conceal('01189998819991197253'))
    print('strikethrough: ' + AnsiFormat.strikethrough('01189998819991197253'))

    print('\nForeground Colors:')
    print('fg_black: ' + AnsiFormat.fg_black('01189998819991197253'))
    print('fg_red: ' + AnsiFormat.fg_red('01189998819991197253'))
    print('fg_green: ' + AnsiFormat.fg_green('01189998819991197253'))
    print('fg_yellow: ' + AnsiFormat.fg_yellow('01189998819991197253'))
    print('fg_blue: ' + AnsiFormat.fg_blue('01189998819991197253'))
    print('fg_magenta: ' + AnsiFormat.fg_magenta('01189998819991197253'))
    print('fg_cyan: ' + AnsiFormat.fg_cyan('01189998819991197253'))
    print('fg_white: ' + AnsiFormat.fg_white('01189998819991197253'))

    print('\nForeground Colors:')
    print('bg_black: ' + AnsiFormat.bg_black('01189998819991197253'))
    print('bg_red: ' + AnsiFormat.bg_red('01189998819991197253'))
    print('bg_green: ' + AnsiFormat.bg_green('01189998819991197253'))
    print('bg_yellow: ' + AnsiFormat.bg_yellow('01189998819991197253'))
    print('bg_blue: ' + AnsiFormat.bg_blue('01189998819991197253'))
    print('bg_magenta: ' + AnsiFormat.bg_magenta('01189998819991197253'))
    print('bg_cyan: ' + AnsiFormat.bg_cyan('01189998819991197253'))
    print('bg_white: ' + AnsiFormat.bg_white('01189998819991197253'))

    print('\nBright Foreground Colors:')
    print('fg_bright_black: ' + AnsiFormat.fg_bright_black('01189998819991197253'))
    print('fg_bright_red: ' + AnsiFormat.fg_bright_red('01189998819991197253'))
    print('fg_bright_green: ' + AnsiFormat.fg_bright_green('01189998819991197253'))
    print('fg_bright_yellow: ' + AnsiFormat.fg_bright_yellow('01189998819991197253'))
    print('fg_bright_blue: ' + AnsiFormat.fg_bright_blue('01189998819991197253'))
    print('fg_bright_magenta: ' + AnsiFormat.fg_bright_magenta('01189998819991197253'))
    print('fg_bright_cyan: ' + AnsiFormat.fg_bright_cyan('01189998819991197253'))
    print('fg_bright_white: ' + AnsiFormat.fg_bright_white('01189998819991197253'))

    print('\nBright Background Colors:')
    print('bg_bright_black: ' + AnsiFormat.bg_bright_black('01189998819991197253'))
    print('bg_bright_red: ' + AnsiFormat.bg_bright_red('01189998819991197253'))
    print('bg_bright_green: ' + AnsiFormat.bg_bright_green('01189998819991197253'))
    print('bg_bright_yellow: ' + AnsiFormat.bg_bright_yellow('01189998819991197253'))
    print('bg_bright_blue: ' + AnsiFormat.bg_bright_blue('01189998819991197253'))
    print('bg_bright_magenta: ' + AnsiFormat.bg_bright_magenta('01189998819991197253'))
    print('bg_bright_cyan: ' + AnsiFormat.bg_bright_cyan('01189998819991197253'))
    print('bg_bright_white: ' + AnsiFormat.bg_bright_white('01189998819991197253'))

    print('\nCombinations:')
    combo = AnsiFormat.underscore(
        AnsiFormat.fg_yellow('0118') +
        AnsiFormat.bg_bright_black('999') +
        AnsiFormat.fg_blue(
            '88199' +
            AnsiFormat.italic(
                '9119' +
                AnsiFormat.invert(
                    '725' +
                    AnsiFormat.strikethrough('3')))))
    print(combo)
    print(AnsiFormat.unformat(combo))
