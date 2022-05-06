from typing import List

from bonus.bonus_card import BonusCard
from bonus.bonus_class import BonusClass
from tree import TreeCard


class Generalist(BonusClass):
    def __init__(self: 'Generalist') -> None:
        super(Generalist, self).__init__(
            name='Generalist',
            description='Gain 10 bonus points for planting the most trees.',
            bonus_points=None,
            experimental=True,
        )

    def count_instance_bonus_points(self: 'Generalist', bonuses: List[BonusCard], all_trees: List[TreeCard]) -> int:
        if BonusCard.LARGEST_ARBORETUM in bonuses:
            return 10
        else:
            return 0
