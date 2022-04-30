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
from typing import List

from pandas import read_csv


class BonusCard:
    def __init__(self, name: str, bonus: int, description: str, visible: bool):
        self.name = name
        self.bonus = bonus if bonus > 0 else None
        self.description = description
        self.visible = visible

    @staticmethod
    def import_visible_from_csv() -> List['BonusCard']:
        _all_bonus_cards = BonusCard._import_all_from_csv()
        return list(filter(lambda bonus_card: bonus_card.visible, _all_bonus_cards))

    @staticmethod
    def _import_all_from_csv() -> List['BonusCard']:
        df = read_csv("data/bonus-cards.csv")
        bonus_cards = df.values.tolist()
        shuffle(bonus_cards)
        return list(map(lambda bonus_card: BonusCard(*bonus_card), bonus_cards))


all_bonus_cards = BonusCard.import_visible_from_csv()


if __name__ == '__main__':
    visible_card_names = list(map(lambda bonus_card: bonus_card.name, all_bonus_cards))

    print('Total Bonus Cards: {}'.format(len(BonusCard._import_all_from_csv())))
    print('Visible Bonus Cards: {}'.format(visible_card_names))
