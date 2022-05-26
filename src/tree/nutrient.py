from enum import Enum

from util.terminal.ansi import AnsiFormat


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
            return AnsiFormat.fg_yellow('🌞')
        elif self == Nutrient.WATER:
            return AnsiFormat.fg_blue('🌊')
        elif self == Nutrient.FIRE:
            return AnsiFormat.fg_red('🔥')
        elif self == Nutrient.DISTURBANCE:
            return AnsiFormat.fg_green('🤘')


if __name__ == '__main__':
    nutrient = Nutrient.FIRE
    print('{} {}'.format(nutrient.emoji(), nutrient))

    nutrients = [nutrient for nutrient in Nutrient]
    nutrients.sort()
    print(' '.join([nutrient.emoji() for nutrient in Nutrient]))
