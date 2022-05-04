from enum import Enum
from random import choice
from typing import List

from tree.tree_card_data import TreeCardData


class Nutrient(Enum):
    SUN = 'sun'
    WATER = 'water'
    FIRE = 'fire'
    DISTURBANCE = 'disturbance'

    @staticmethod
    def random() -> 'Nutrient':
        nutrient_pool: List[Nutrient] = [
            *(5 * [Nutrient.SUN]),
            *(2 * [Nutrient.WATER]),
            *(1 * [Nutrient.FIRE]),
            *(1 * [Nutrient.DISTURBANCE]),
        ]
        return choice(nutrient_pool)

    @staticmethod
    def list_from_tree_card_data(tree_card_data: TreeCardData) -> List['Nutrient']:
        return [
            *(tree_card_data.sun * [Nutrient.SUN]),
            *(tree_card_data.water * [Nutrient.WATER]),
            *(tree_card_data.fire * [Nutrient.FIRE]),
            *(tree_card_data.disturbance * [Nutrient.DISTURBANCE]),
        ]

    def __lt__(self: 'Nutrient', other: 'Nutrient') -> bool:
        return self.__get_sort_order() < other.__get_sort_order()

    def __get_sort_order(self: 'Nutrient') -> int:
        if self == Nutrient.SUN:
            return 0
        elif self == Nutrient.WATER:
            return 1
        elif self == Nutrient.FIRE:
            return 2
        elif self == Nutrient.DISTURBANCE:
            return 3

    def to_emoji(self: 'Nutrient') -> str:
        if self == Nutrient.SUN:
            return '🌞'
        elif self == Nutrient.WATER:
            return '🌊'
        elif self == Nutrient.FIRE:
            return '🔥'
        elif self == Nutrient.DISTURBANCE:
            return '🤘'


if __name__ == '__main__':
    nutrient = Nutrient.random()
    print('{} {}'.format(nutrient.to_emoji(), nutrient))

    nutrients = [Nutrient.random().to_emoji() for i in range(10)]
    nutrients.sort()
    print(' '.join(nutrients))
