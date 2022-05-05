from game import Move


def get_move() -> Move:
    move_string = input_move()
    move = Move.from_string(move_string)
    while move is None:
        print('Invalid Move: {}. Please try again.'.format(move_string))
        move_string = input_move()
        move = Move.from_string(move_string)
    return move


def input_move() -> str:
    return input(
        'Select from the following options:\n' +
        '  1. Plant a tree\n' +
        '  2. Hug some trees\n' +
        '  3. Draw nutrients\n' +
        '  4. Draw tree cards\n' +
        '  5. Skip your turn\n'
        '  → ')


if __name__ == '__main__':
    print(get_move())
