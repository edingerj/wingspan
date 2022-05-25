from sys import stdout

from gameplay.console.runtime.sleep import sleep
from util.terminal.ansi import LINE_CLEAR, LINE_UP


def clear_lines(lines: int = 1) -> None:
    """ Requires terminal emulation in PyCharm """
    for _ in range(lines):
        print(LINE_UP, end=LINE_CLEAR)
    stdout.flush()


def print_line() -> None:
    print(80 * '─')
    sleep(0.5)


def input_line() -> None:
    input(80 * '─')
    sleep(0.5)


def print_ellipsis(delay: float = 0.5, end: str = '\n') -> None:
    for _ in range(3):
        print('.', end='')
        stdout.flush()
        sleep(delay)
    if end != '':
        print('', end=end)


__all__ = [
    'clear_lines',
    'print_line',
    'input_line',
    'print_ellipsis',
]


if __name__ == '__main__':
    for i in range(10):
        print(i)
        sleep(1)
        clear_lines()
    print('Done')
