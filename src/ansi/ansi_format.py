from typing import Final

from ansi.escape_characters import *


class AnsiFormat:
    """
    Accounts for the length of added ANSI escape characters
    when using length formatting utilities like str.ljust()
    """
    ATTR_LEN_OFFSET: Final[int] = 9
    COLOR_LEN_OFFSET: Final[int] = 10

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
    def black(text: str) -> str:
        return '{}{}{}'.format(BLACK, text, FOREGROUND_OFF)

    @staticmethod
    def red(text: str) -> str:
        return '{}{}{}'.format(RED, text, FOREGROUND_OFF)

    @staticmethod
    def green(text: str) -> str:
        return '{}{}{}'.format(GREEN, text, FOREGROUND_OFF)

    @staticmethod
    def yellow(text: str) -> str:
        return '{}{}{}'.format(YELLOW, text, FOREGROUND_OFF)

    @staticmethod
    def blue(text: str) -> str:
        return '{}{}{}'.format(BLUE, text, FOREGROUND_OFF)

    @staticmethod
    def magenta(text: str) -> str:
        return '{}{}{}'.format(MAGENTA, text, FOREGROUND_OFF)

    @staticmethod
    def cyan(text: str) -> str:
        return '{}{}{}'.format(CYAN, text, FOREGROUND_OFF)

    @staticmethod
    def white(text: str) -> str:
        return '{}{}{}'.format(WHITE, text, FOREGROUND_OFF)
    # endregion Foreground Colors

    # region Bright Foreground Colors
    @staticmethod
    def bright_black(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_BLACK, text, FOREGROUND_OFF)

    @staticmethod
    def bright_red(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_RED, text, FOREGROUND_OFF)

    @staticmethod
    def bright_green(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_GREEN, text, FOREGROUND_OFF)

    @staticmethod
    def bright_yellow(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_YELLOW, text, FOREGROUND_OFF)

    @staticmethod
    def bright_blue(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_BLUE, text, FOREGROUND_OFF)

    @staticmethod
    def bright_magenta(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_MAGENTA, text, FOREGROUND_OFF)

    @staticmethod
    def bright_cyan(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_CYAN, text, FOREGROUND_OFF)

    @staticmethod
    def bright_white(text: str) -> str:
        return '{}{}{}'.format(BRIGHT_WHITE, text, FOREGROUND_OFF)
    # endregion Bright Foreground Colors


if __name__ == '__main__':
    print('\nText Attributes:')
    print('BOLD: ' + AnsiFormat.bold('01189998819991197253'))
    print('FAINT: ' + AnsiFormat.faint('01189998819991197253'))
    print('ITALIC: ' + AnsiFormat.italic('01189998819991197253'))
    print('UNDERSCORE: ' + AnsiFormat.underscore('01189998819991197253'))
    print('BLINK: ' + AnsiFormat.blink('01189998819991197253'))
    print('INVERT: ' + AnsiFormat.invert('01189998819991197253'))
    print('CONCEAL: ' + AnsiFormat.conceal('01189998819991197253'))
    print('STRIKETHROUGH: ' + AnsiFormat.strikethrough('01189998819991197253'))

    print('\nForeground Colors:')
    print('BLACK: ' + AnsiFormat.black('01189998819991197253'))
    print('RED: ' + AnsiFormat.red('01189998819991197253'))
    print('GREEN: ' + AnsiFormat.green('01189998819991197253'))
    print('YELLOW: ' + AnsiFormat.yellow('01189998819991197253'))
    print('BLUE: ' + AnsiFormat.blue('01189998819991197253'))
    print('MAGENTA: ' + AnsiFormat.magenta('01189998819991197253'))
    print('CYAN: ' + AnsiFormat.cyan('01189998819991197253'))
    print('WHITE: ' + AnsiFormat.white('01189998819991197253'))

    print('\nBright Foreground Colors:')
    print('BRIGHT_BLACK: ' + AnsiFormat.bright_black('01189998819991197253'))
    print('BRIGHT_RED: ' + AnsiFormat.bright_red('01189998819991197253'))
    print('BRIGHT_GREEN: ' + AnsiFormat.bright_green('01189998819991197253'))
    print('BRIGHT_YELLOW: ' + AnsiFormat.bright_yellow('01189998819991197253'))
    print('BRIGHT_BLUE: ' + AnsiFormat.bright_blue('01189998819991197253'))
    print('BRIGHT_MAGENTA: ' + AnsiFormat.bright_magenta('01189998819991197253'))
    print('BRIGHT_CYAN: ' + AnsiFormat.bright_cyan('01189998819991197253'))
    print('BRIGHT_WHITE: ' + AnsiFormat.bright_white('01189998819991197253'))

    print('\nCombinations:')
    print(AnsiFormat.underscore(
        AnsiFormat.yellow('0118') +
        AnsiFormat.bright_yellow('999') +
        AnsiFormat.blue(
            '88199' +
            AnsiFormat.italic(
                '9119' +
                AnsiFormat.invert(
                    '725' +
                    AnsiFormat.strikethrough('3'))))))
