from enum import Enum
from typing import Optional


class Info(Enum):
    DISPLAY_HAND = 'DISPLAY_HAND'
    DISPLAY_TOP_DECK = 'DISPLAY_TOP_DECK'
    DISPLAY_BONUSES = 'DISPLAY_BONUSES'
    CONTINUE = 'CONTINUE'

    @staticmethod
    def from_string(info_string: str) -> Optional['Info']:
        if info_string == '1':
            return Info.DISPLAY_HAND
        elif info_string == '2':
            return Info.DISPLAY_TOP_DECK
        elif info_string == '3':
            return Info.DISPLAY_BONUSES
        elif info_string == '4':
            return Info.CONTINUE
        else:
            return None


if __name__ == '__main__':
    print(Info.from_string('1'))
