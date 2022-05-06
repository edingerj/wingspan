"""
Bonus Class Ideas:
  · Michigander
  · tree hugger
  · tree climber
  · pyrosilviculture enthusiast
  · fake tree lover
  · utility forester
  · tree trimmer
  · generalist
  · food type
"""

from abc import ABCMeta, abstractmethod
from typing import Final, Optional, List

from bonus.bonus_card import BonusCard
from tree import TreeCard


class BonusClass(metaclass=ABCMeta):
    def __init__(self: 'BonusClass', name: str, description: str,
                 bonus_points: Optional[int], experimental: bool) -> None:
        self.name: Final[str] = name
        self.description: Final[str] = description
        self.bonus_points: Final[Optional[int]] = bonus_points
        self.experimental: Final[bool] = experimental

    def count_bonus_points(self: 'BonusClass', bonuses: List[BonusCard], all_trees: List[TreeCard]) -> int:
        return self.count_generic_bonus_points(bonuses) \
            + self.count_instance_bonus_points(bonuses, all_trees)

    @staticmethod
    def count_generic_bonus_points(bonuses: List[BonusCard]) -> int:
        if BonusCard.TALLEST_ARBORETUM in bonuses:
            return 10
        else:
            return 0

    @abstractmethod
    def count_instance_bonus_points(self: 'BonusClass', bonuses: List[BonusCard], all_trees: List[TreeCard]) -> int:
        pass

    def __str__(self: 'BonusClass') -> str:
        return '{}: {}'.format(self.name, self.description)
