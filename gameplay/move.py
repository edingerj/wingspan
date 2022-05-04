from enum import Enum
from typing import Optional


class Move(Enum):
    PLANT_TREE = 'plant tree'
    HUG_TREES = 'hug trees'
    DRAW_NUTRIENTS = 'draw nutrients'
    DRAW_TREES = 'draw trees'
    SKIP_TURN = 'skip turn'

    @staticmethod
    def from_string(move_string: str) -> Optional['Move']:
        if move_string == '1':
            return Move.PLANT_TREE
        elif move_string == '2':
            return Move.HUG_TREES
        elif move_string == '3':
            return Move.DRAW_NUTRIENTS
        elif move_string == '4':
            return Move.DRAW_TREES
        elif move_string == '5':
            return Move.SKIP_TURN
        else:
            return None

    @staticmethod
    def input_move() -> 'Move':
        move_string = input(
            'Select from the following options:\n' +
            '  1. Plant a tree\n' +
            '  2. Hug some trees\n' +
            '  3. Draw nutrients\n' +
            '  4. Draw tree cards\n' +
            '  5. Skip your turn\n'
            '  → ')
        move = Move.from_string(move_string)

        if move is not None:
            return move
        else:
            print('Invalid Move: {}. Please try again.'.format(move_string))
            return Move.input_move()


if __name__ == '__main__':
    print(Move.input_move())
