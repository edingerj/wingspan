"""
Dependencies: pandas

Bonus Card Ideas:
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

from random import shuffle
from typing import Final, List, Optional

from pandas import read_csv

from bonus.bonus_card_data import BonusCardData


class BonusCard:
    def __init__(self: 'BonusCard', name: str, description: str, bonus_points: Optional[int], visible: bool):
        self.name: Final[str] = name
        self.description: Final[str] = description
        self.bonus_points: Final[Optional[int]] = bonus_points
        self.visible: Final[bool] = visible

    @staticmethod
    def import_visible_from_csv() -> List['BonusCard']:
        all_bonus_cards = BonusCard.import_all_from_csv()
        return list(filter(lambda bonus_card: bonus_card.visible, all_bonus_cards))

    @staticmethod
    def import_all_from_csv() -> List['BonusCard']:
        card_data: Final[List[BonusCardData]] = list(map(BonusCardData.of, read_csv('data/bonus-cards.csv').values))
        shuffle(card_data)
        return list(map(BonusCard.from_card_data, card_data))

    @staticmethod
    def from_card_data(card_data: BonusCardData) -> 'BonusCard':
        bonus_points: Final[Optional[int]] = card_data.bonus_points if (card_data.bonus_points > 0) else None
        return BonusCard(card_data.name, card_data.description, bonus_points, card_data.visible)


if __name__ == '__main__':
    visible_bonus_cards = BonusCard.import_visible_from_csv()
    visible_card_names = list(map(lambda bonus_card: bonus_card.name, visible_bonus_cards))

    print('Total Bonus Cards: {}'.format(len(BonusCard.import_all_from_csv())))
    print('Visible Bonus Cards: {}'.format(visible_card_names))
