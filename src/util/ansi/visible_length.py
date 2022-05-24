from unicodedata import east_asian_width

from util.ansi.ansi_format import AnsiFormat


def visible_character_length(character: str) -> int:
    """
    :return: Two spaces for a "wide" character, one space for others.
    """
    return 2 if (east_asian_width(character) == 'W') else 1


def visible_length(text: str) -> int:
    """
    Returns the width of printed (non-escape) characters in a string,
    as they will appear in a terminal.
    """

    unformatted_text = AnsiFormat.unformat(text)
    return sum([visible_character_length(character) for character in unformatted_text])


def visible_offset(text: str) -> int:
    return visible_length(text) - len(text)
