"""
Dependencies: pandas
"""

from typing import List, NamedTuple, Tuple

from pandas import read_csv


class BonusCardData(NamedTuple):
    name: str
    bonus_points: int
    description: str
    experimental: bool

    @staticmethod
    def import_all_from_csv() -> List['BonusCardData']:
        return list(map(BonusCardData.of, read_csv('data/bonus_classes.csv').values))

    @staticmethod
    def of(bonus_card_data: Tuple[str, int, str, bool]) -> 'BonusCardData':
        return BonusCardData(*bonus_card_data)


if __name__ == '__main__':
    _bonus_card_data = BonusCardData.import_all_from_csv()
    print(_bonus_card_data)
