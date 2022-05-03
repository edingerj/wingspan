from enum import Enum
from random import choice
from typing import List

from tree_card_data import TreeCardData


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


if __name__ == '__main__':
    print(Nutrient.random())
