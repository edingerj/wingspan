from collections import Counter
from typing import List

from bonus.bonus_card import BonusCard
from bonus.bonus_token import BonusToken
from tree import Habitat, TreeCard


class Generalist(BonusCard):
    def __init__(self: 'Generalist') -> None:
        super(Generalist, self).__init__(
            name='Generalist',
            description='Gain 5 bonus points for each planted tree in your smallest habitat.',
            bonus_points=None,
            experimental=True,
        )

    def count_instance_bonus_points(self: 'Generalist', bonuses: List[BonusToken], all_trees: List[TreeCard]) -> int:
        planted_habitat_sizes = Counter([tree_card.habitat for tree_card in all_trees])
        habitat_sizes = {habitat: planted_habitat_sizes[habitat] for habitat in Habitat}
        smallest_habitat_size = min(habitat_sizes.values(), default=0)
        return 5 * smallest_habitat_size
