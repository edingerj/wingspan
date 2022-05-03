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
from typing import List, Optional, Union, Final

from pandas import read_csv


class BonusCard:
    def __init__(self: 'BonusCard', name: str, bonus_points: int, description: str, visible: bool):
        self.name: str = name
        self.description: str = description
        self.bonus_points: Optional[int] = bonus_points if (bonus_points > 0) else None
        self.visible: bool = visible

    @staticmethod
    def import_visible_from_csv() -> List['BonusCard']:
        all_bonus_cards = BonusCard.import_all_from_csv()
        return list(filter(lambda bonus_card: bonus_card.visible, all_bonus_cards))

    @staticmethod
    def import_all_from_csv() -> List['BonusCard']:
        bonus_cards: Final[List[Union[str, int]]] = read_csv('data/bonus-cards.csv').values.tolist()
        shuffle(bonus_cards)
        return list(map(lambda bonus_card: BonusCard(*bonus_card), bonus_cards))


if __name__ == '__main__':
    visible_bonus_cards = BonusCard.import_visible_from_csv()
    visible_card_names = list(map(lambda bonus_card: bonus_card.name, visible_bonus_cards))

    print('Total Bonus Cards: {}'.format(len(BonusCard.import_all_from_csv())))
    print('Visible Bonus Cards: {}'.format(visible_card_names))
