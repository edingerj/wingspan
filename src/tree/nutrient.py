from enum import Enum

from unicodedata import east_asian_width


class Nutrient(Enum):
    SUN = 'SUN'
    WATER = 'WATER'
    FIRE = 'FIRE'
    DISTURBANCE = 'DISTURBANCE'

    def __lt__(self: 'Nutrient', other: 'Nutrient') -> bool:
        return self.__get_sort_order() < other.__get_sort_order()

    def __get_sort_order(self: 'Nutrient') -> int:
        if self == Nutrient.SUN:
            return 0
        elif self == Nutrient.WATER:
            return 1
        elif self == Nutrient.FIRE:
            return 2
        elif self == Nutrient.DISTURBANCE:
            return 3

    def emoji(self: 'Nutrient') -> str:
        if self == Nutrient.SUN:
            return '🌞'
        elif self == Nutrient.WATER:
            return '🌊'
        elif self == Nutrient.FIRE:
            return '🔥'
        elif self == Nutrient.DISTURBANCE:
            return '🤘'


if __name__ == '__main__':
    nutrient = Nutrient.FIRE
    print('{} {}'.format(nutrient.emoji(), nutrient))

    def visible_length(unicode_string: str) -> int:
        """ Two spaces for "wide" characters, one space for others. """
        return sum([2 if (east_asian_width(char) == 'W') else 1 for char in unicode_string])

    nutrients = [nutrient for nutrient in Nutrient]
    nutrients.sort()
    nutrient_emojis = ' '.join([nutrient.emoji() for nutrient in Nutrient])
    print(nutrient_emojis)
    print('len: {}, visible_length: {}'.format(len(nutrient_emojis), visible_length(nutrient_emojis)))
