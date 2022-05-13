from util.ansi import AnsiColor

DELIMITER = '│'


def delimiter(color=AnsiColor.DEFAULT) -> str:
    return color.foreground(DELIMITER)
