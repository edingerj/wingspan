from enum import Enum


class Habitat(Enum):
    CONIFEROUS = 'CONIFEROUS'
    DECIDUOUS = 'DECIDUOUS'
    URBAN = 'URBAN'

    @staticmethod
    def from_string(habitat_str: str) -> 'Habitat':
        if habitat_str == 'CONIFEROUS':
            return Habitat.CONIFEROUS
        elif habitat_str == 'DECIDUOUS':
            return Habitat.DECIDUOUS
        elif habitat_str == 'URBAN':
            return Habitat.URBAN

    def to_string(self: 'Habitat') -> str:
        if self is Habitat.CONIFEROUS:
            return 'Coniferous'
        if self is Habitat.DECIDUOUS:
            return 'Deciduous'
        if self is Habitat.URBAN:
            return 'Urban'


if __name__ == '__main__':
    print(Habitat.from_string('DECIDUOUS'))
    print([habitat.to_string() for habitat in Habitat])
