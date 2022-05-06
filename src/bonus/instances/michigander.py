from typing import List

from bonus.bonus import Bonus
from bonus.bonus_class import BonusClass
from tree import TreeCard


class Michigander(BonusClass):
    def __init__(self: 'Michigander') -> None:
        super(Michigander, self).__init__(
            name='Michigander',
            description='Gain 2 bonus points for each planted tree that is found in Michigan.',
            bonus_points=None,
            experimental=False,
        )

    def count_instance_bonus_points(self: 'Michigander', bonuses: List[Bonus], all_trees: List[TreeCard]) -> int:
        michiganders = list(filter(lambda tree_card: tree_card.michigander, all_trees))
        return 2 * len(michiganders)
