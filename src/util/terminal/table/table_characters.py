from util.terminal.ansi import AnsiColor

DELIMITER = '│'


def delimiter(delimiter_color=AnsiColor.DEFAULT) -> str:
    return delimiter_color.foreground(DELIMITER)
