"""
Dependencies: pandas
"""

from typing import List, NamedTuple, Tuple

from pandas import read_csv


class BonusClassData(NamedTuple):
    name: str
    bonus_points: int
    description: str
    experimental: bool

    @staticmethod
    def import_all_from_csv() -> List['BonusClassData']:
        return list(map(BonusClassData.of, read_csv('data/bonus_classes.csv').values))

    @staticmethod
    def of(bonus_card_data: Tuple[str, int, str, bool]) -> 'BonusClassData':
        return BonusClassData(*bonus_card_data)


if __name__ == '__main__':
    _bonus_card_data = BonusClassData.import_all_from_csv()
    print(_bonus_card_data)
