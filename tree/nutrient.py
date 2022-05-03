from enum import Enum
from random import choice
from typing import List

from tree.tree_card_def import TreeCardDef


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
    def list_from_tree_card_def(tree_card_def: TreeCardDef) -> List['Nutrient']:
        return [
            *(tree_card_def.sun * [Nutrient.SUN]),
            *(tree_card_def.water * [Nutrient.WATER]),
            *(tree_card_def.fire * [Nutrient.FIRE]),
            *(tree_card_def.disturbance * [Nutrient.DISTURBANCE]),
        ]


if __name__ == '__main__':
    print(Nutrient.random())
