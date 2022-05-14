from typing import Iterable, List, Optional

from bonus.bonus_card import BonusCard
from bonus.instances import *


class BonusCards(List[BonusCard]):
    def __init__(self: 'BonusCards', bonus_cards: Iterable[BonusCard] = ()) -> None:
        super(BonusCards, self).__init__(bonus_cards)

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

    # where choice can be a bonus card name, or a 1 index
    def index_of(self: 'BonusCards', choice: str) -> Optional[int]:
        bonus_card: Optional[BonusCard] = \
            next(filter(lambda card: card.name.lower() == choice.lower(), self), None)
        if bonus_card is not None:
            return self.index(bonus_card)
        try:
            index = int(choice) - 1
            return index if (index < len(self)) else None
        except ValueError:
            return None

    def table_format(self: 'BonusCards') -> str:
        return '\n'.join(['  {} {}'.format(
            '{}.'.format(index + 1).ljust(3),
            '{}'.format(bonus_class.table_format()),
        ) for index, bonus_class in enumerate(self)])


if __name__ == '__main__':
    print(BonusCards.all())
