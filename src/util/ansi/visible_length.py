from unicodedata import east_asian_width

from util.ansi.ansi_format import AnsiFormat


def visible_length(text: str) -> int:
    """
    Remove any formatted ansi escape characters
    :return Two spaces for each "wide" character, one space for others.
    """
    unformatted_text = AnsiFormat.unformat(text)
    return sum([2 if (east_asian_width(char) == 'W') else 1 for char in unformatted_text])


def visible_offset(text: str) -> int:
    return visible_length(text) - len(text)
