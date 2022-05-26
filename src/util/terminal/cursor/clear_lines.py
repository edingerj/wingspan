from sys import stdout
from time import sleep

from util.terminal.ansi import LINE_CLEAR, LINE_UP


def clear_lines(lines: int = 1) -> None:
    """ Requires terminal emulation in PyCharm """
    print(f'\r{LINE_CLEAR}' + f'{LINE_UP}{LINE_CLEAR}' * lines, end='')
    stdout.flush()


if __name__ == '__main__':
    for i in range(5):
        print(i)
        sleep(1)
        clear_lines()
    print('Done')
    sleep(1)

    print('*****\n*   *\n*   *\n*   *\n*****')
    sleep(1)
    clear_lines(5)
