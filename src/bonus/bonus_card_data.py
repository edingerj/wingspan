from typing import NamedTuple, Tuple


class BonusCardData(NamedTuple):
    name: str
    bonus_points: int
    description: str
    visible: bool

    @staticmethod
    def of(bonus_card_data: Tuple[str, int, str, bool]) -> 'BonusCardData':
        return BonusCardData(*bonus_card_data)
