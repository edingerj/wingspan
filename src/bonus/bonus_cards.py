from random import shuffle
from typing import Iterable, List

from bonus.instances import *
from bonus.bonus_card import BonusCard


class BonusCards(List[BonusCard]):
    def __init__(self: 'BonusCards', bonus_classes: Iterable[BonusCard] = ()) -> None:
        super(BonusCards, self).__init__(bonus_classes)
        shuffle(self)

    @staticmethod
    def all() -> 'BonusCards':
        return BonusCards([
            Generalist(),
            Michigander(),
            TreeClimber(),
            TreeHugger(),
        ])

    @staticmethod
    def established() -> 'BonusCards':
        return BonusCards(filter(lambda bonus_class: bonus_class.experimental is False, BonusCards.all()))

    def __str__(self: 'BonusCards') -> str:
        return '\n'.join([
            '  {}. {}'.format(index + 1, bonus_class)
            for index, bonus_class in enumerate(self)
        ])


if __name__ == '__main__':
    _bonus_classes = BonusCards.all()
    print(_bonus_classes)
