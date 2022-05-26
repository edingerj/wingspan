from unicodedata import east_asian_width

from util.terminal.ansi.ansi_format import AnsiFormat
from util.terminal.cursor.clear_lines import clear_lines
from util.terminal.cursor.cursor_position import cursor_position


class VisibleText:
    EMOJI_WIDTH = 2

    @staticmethod
    def calculate_emoji_width() -> None:
        (start_position, _) = cursor_position()
        print('🌞', end='')
        (end_position, _) = cursor_position()
        clear_lines(0)
        VisibleText.EMOJI_WIDTH = end_position - start_position

    @staticmethod
    def character_length(character: str) -> int:
        """
        :return: Two spaces for a "wide" character, one space for others.
        """
        return VisibleText.EMOJI_WIDTH if (east_asian_width(character) == 'W') else 1

    @staticmethod
    def length(text: str) -> int:
        """
        :return: the width of printed (non-escape) characters in a string,
        as they will appear in a terminal.
        """
        unformatted_text = AnsiFormat.unformat(text)
        return sum([VisibleText.character_length(character) for character in unformatted_text])

    @staticmethod
    def offset(text: str) -> int:
        """
        :return: the difference of the width of printed (non-escape) characters in a string,
        as they will appear in a terminal, and the normal length of the string.
        """
        return VisibleText.length(text) - len(text)


if __name__ == '__main__':
    print('default emoji width: {}px'.format(VisibleText.EMOJI_WIDTH))
    VisibleText.calculate_emoji_width()
    print('actual emoji width: {}px'.format(VisibleText.EMOJI_WIDTH))
