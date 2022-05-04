from enum import Enum


class Habitat(Enum):
    CONIFER = 'Conifer'
    DECIDUOUS = 'Deciduous'
    URBAN = 'Urban'

    @staticmethod
    def from_string(habitat_str: str) -> 'Habitat':
        if habitat_str == 'Conifer':
            return Habitat.CONIFER
        elif habitat_str == 'Deciduous':
            return Habitat.DECIDUOUS
        elif habitat_str == 'Urban':
            return Habitat.URBAN


if __name__ == '__main__':
    print(Habitat.from_string('Conifer'))
