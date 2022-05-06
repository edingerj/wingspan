from typing import List

from bonus.bonus_card import BonusCard
from bonus.bonus_class import BonusClass
from tree import TreeCard


class TreeHugger(BonusClass):
    def __init__(self: 'TreeHugger') -> None:
        super(TreeHugger, self).__init__(
            name='Tree Hugger',
            description='Gain 10 bonus points for hugging the most trees.',
            bonus_points=10,
            experimental=True,
        )

    def count_instance_bonus_points(self: 'TreeHugger', bonuses: List[BonusCard], all_trees: List[TreeCard]) -> int:
        if BonusCard.MOST_TREES_HUGGED in bonuses:
            return 10
        else:
            return 0
