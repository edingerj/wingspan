from sys import stdout

from gameplay.console.runtime.sleep import sleep


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
    'print_line',
    'input_line',
    'print_ellipsis',
]
