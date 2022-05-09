from random import choice
from typing import Iterable, List

from tree.nutrient import Nutrient
from tree.tree_card_data import TreeCardData


class Nutrients(List[Nutrient]):
    def __init__(self: 'Nutrients', nutrients: Iterable[Nutrient] = ()) -> None:
        super(Nutrients, self).__init__(nutrients)

    @staticmethod
    def random_sorted(size: int = 3) -> 'Nutrients':
        nutrients = Nutrients.random(size)
        nutrients.sort()
        return nutrients

    @staticmethod
    def random(size: int = 3) -> 'Nutrients':
        nutrient_pool = Nutrients.get_nutrient_pool()
        return Nutrients([choice(nutrient_pool) for _ in range(size)])

    @staticmethod
    def get_nutrient_pool() -> 'Nutrients':
        return Nutrients([
            *(5 * [Nutrient.SUN]),
            *(2 * [Nutrient.WATER]),
            *(1 * [Nutrient.FIRE]),
            *(1 * [Nutrient.DISTURBANCE]),
        ])

    @staticmethod
    def from_tree_card_data(tree_card_data: TreeCardData) -> 'Nutrients':
        return Nutrients([
            *(tree_card_data.sun * [Nutrient.SUN]),
            *(tree_card_data.water * [Nutrient.WATER]),
            *(tree_card_data.fire * [Nutrient.FIRE]),
            *(tree_card_data.disturbance * [Nutrient.DISTURBANCE]),
        ])

    def extend(self: 'Nutrients', __iterable: Iterable[Nutrient]) -> None:
        super(Nutrients, self).extend(__iterable)
        self.sort()

    def emoji_format(self: 'Nutrients') -> str:
        return ' '.join([nutrient.emoji() for nutrient in self])


if __name__ == '__main__':
    print(Nutrients.random(10))
    print(Nutrients.random_sorted(10))
