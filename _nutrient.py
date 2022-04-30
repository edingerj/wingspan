from enum import Enum
from random import choice
from typing import List


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


if __name__ == '__main__':
    print(Nutrient.random())
