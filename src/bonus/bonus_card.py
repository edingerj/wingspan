"""
Bonus Class Ideas:
  Implemented
  · Ecologist (generalist)
  · Michigander
  · tree hugger
  · tree climber

  Unimplemented
  · pyrosilviculture enthusiast
  · (water quality) analyst - silly name required
  · fake tree lover - 2 points for each low value tree (
  · utility forester - commonly occur under power lines
  · tree trimmer - fast-growing trees (add to csv as FAST, MEDIUM, SLOW)
  · foodie (omnivore expert in ws) - 2 for each wildcard nutrient
  · photographer - trees with color names, like "redwood" (add to csv)
  · cartographer - trees with geography names, like "Eastern redcedar" (add to csv)
  · tree sniffer - 4 points for each scented tree (add to csv)
  · tree counter - 2 points for each planted tree with a tucking power
  · visionary - 4 points for 5+, 7 points for 8+ tree cards in hand at end of game
  ·
  ·

  Expansion Pack: Fake Trees, using fake_trees.csv
  · very fake tree lover - rewards for actually fake trees.
  · historian - trees with people names, like "steve" (add to csv)
"""

from abc import ABCMeta, abstractmethod
from typing import Final, Optional, List

from bonus.bonus_token import BonusToken
from tree import TreeCard


class BonusCard(metaclass=ABCMeta):
    def __init__(self: 'BonusCard', name: str, description: str,
                 bonus_points: Optional[int], experimental: bool) -> None:
        self.name: Final[str] = name
        self.description: Final[str] = description
        self.bonus_points: Final[Optional[int]] = bonus_points
        self.experimental: Final[bool] = experimental

    def count_bonus_points(self: 'BonusCard', bonuses: List[BonusToken], all_trees: List[TreeCard]) -> int:
        return self.count_generic_bonus_points(bonuses) + \
               self.count_instance_bonus_points(bonuses, all_trees)

    @staticmethod
    def count_generic_bonus_points(bonuses: List[BonusToken]) -> int:
        if BonusToken.TALLEST_ARBORETUM in bonuses:
            return 10
        else:
            return 0

    @abstractmethod
    def count_instance_bonus_points(self: 'BonusCard', bonuses: List[BonusToken], all_trees: List[TreeCard]) -> int:
        pass

    def table_format(self: 'BonusCard') -> str:
        return '{}: {}'.format(self.name, self.description)
