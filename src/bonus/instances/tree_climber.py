from typing import List

from bonus.bonus import Bonus
from bonus.bonus_class import BonusClass
from tree import TreeCard


class TreeClimber(BonusClass):
    def __init__(self: 'TreeClimber') -> None:
        super(TreeClimber, self).__init__(
            name='Tree Climber',
            description='Gain 10 bonus points for planting the tallest combined height of trees.',
            bonus_points=10,
            experimental=False,
        )

    def count_instance_bonus_points(self: 'TreeClimber', bonuses: List[Bonus], all_trees: List[TreeCard]) -> int:
        if Bonus.TALLEST_ARBORETUM in bonuses:
            return 10
        else:
            return 0
