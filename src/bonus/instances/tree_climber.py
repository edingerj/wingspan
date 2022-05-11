from typing import List

from bonus.bonus_card import BonusCard
from bonus.bonus_token import BonusToken
from tree import TreeCard


class TreeClimber(BonusCard):
    def __init__(self: 'TreeClimber') -> None:
        super(TreeClimber, self).__init__(
            name='Tree Climber',
            description='Gain 10 bonus points for planting the tallest combined height of trees.',
            bonus_points=10,
            experimental=False,
        )

    def count_instance_bonus_points(self: 'TreeClimber', bonuses: List[BonusToken], all_trees: List[TreeCard]) -> int:
        if BonusToken.TALLEST_ARBORETUM in bonuses:
            return 10
        else:
            return 0
