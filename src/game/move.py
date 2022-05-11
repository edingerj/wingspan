from enum import Enum
from typing import Optional


class Move(Enum):
    PLANT_TREE = 'plant tree'
    HUG_TREES = 'hug trees'
    DRAW_NUTRIENTS = 'draw nutrients'
    DRAW_TREES = 'draw trees'
    CONTINUE = 'skip move'

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
            return Move.CONTINUE
        else:
            return None


if __name__ == '__main__':
    print(Move.from_string('1'))
