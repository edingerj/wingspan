from random import shuffle
from typing import Iterable, List

from bonus.instances import *
from bonus.bonus_class import BonusClass


class BonusClasses(List[BonusClass]):
    def __init__(self: 'BonusClasses', bonus_classes: Iterable[BonusClass] = ()) -> None:
        super(BonusClasses, self).__init__(bonus_classes)
        shuffle(self)

    @staticmethod
    def all() -> 'BonusClasses':
        return BonusClasses([
            Generalist(),
            Michigander(),
            TreeClimber(),
            TreeHugger(),
        ])

    @staticmethod
    def established() -> 'BonusClasses':
        return BonusClasses(filter(lambda bonus_class: bonus_class.experimental is False, BonusClasses.all()))

    def __str__(self: 'BonusClasses') -> str:
        return '\n'.join([
            '  {}. {}'.format(index + 1, bonus_class)
            for index, bonus_class in enumerate(self)
        ])


if __name__ == '__main__':
    _bonus_classes = BonusClasses.all()
    print(_bonus_classes)
