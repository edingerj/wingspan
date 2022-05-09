from typing import List

from bonus.bonus_card import BonusCard
from bonus.bonus_token import BonusToken
from tree import TreeCard


class Michigander(BonusCard):
    def __init__(self: 'Michigander') -> None:
        super(Michigander, self).__init__(
            name='Michigander',
            description='Gain 2 bonus points for each planted tree that is found in Michigan.',
            bonus_points=None,
            experimental=False,
        )

    def count_instance_bonus_points(self: 'Michigander', bonuses: List[BonusToken], all_trees: List[TreeCard]) -> int:
        michiganders = list(filter(lambda tree_card: tree_card.michigander, all_trees))
        return 2 * len(michiganders)
