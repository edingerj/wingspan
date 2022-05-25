from re import match
from sys import platform, stdin, stdout

if platform == 'win32':
    from ctypes import byref, windll, wintypes
else:
    from termios import ECHO, ICANON, tcgetattr, tcsetattr, TCSAFLUSH


def cursor_position() -> (int, int):
    """
    NOTE: positional indexing begins at 1.

    :return: an (x, y) tuple of the current terminal cursor position.
    :except: In the event of an error reading from the stdin, returns (-1, -1)
    """

    if platform == 'win32':
        old_stdin_mode = wintypes.DWORD()
        old_stdout_mode = wintypes.DWORD()
        kernel32 = windll.kernel32
        kernel32.GetConsoleMode(kernel32.GetStdHandle(-10), byref(old_stdin_mode))
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 0)
        kernel32.GetConsoleMode(kernel32.GetStdHandle(-11), byref(old_stdout_mode))
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        old_stdin_mode = tcgetattr(stdin)
        new_stdin_mode = tcgetattr(stdin)
        new_stdin_mode[3] = new_stdin_mode[3] & ~(ECHO | ICANON)
        tcsetattr(stdin, TCSAFLUSH, new_stdin_mode)

    try:
        buffer = ''
        stdout.write('\x1b[6n')
        stdout.flush()
        while not (buffer := buffer + stdin.read(1)).endswith('R'):
            pass
        matches = match(r'^\x1b\[(?P<y>\d*);(?P<x>\d*)R', buffer)
    finally:
        if platform == 'win32':
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), old_stdin_mode)
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), old_stdout_mode)
        else:
            tcsetattr(stdin, TCSAFLUSH, old_stdin_mode)

    if matches:
        return int(matches.group('x')), int(matches.group('y'))
    else:
        return -1, -1


if __name__ == '__main__':
    x, y = cursor_position()
    print(f'Cursor x: {x}, y: {y}')

    print('🌞', end='')
    x, y = cursor_position()
    print(f'Cursor x: {x}, y: {y}')
