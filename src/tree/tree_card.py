from typing import Final

from tree.habitat import Habitat
from tree.nutrients import Nutrients
from tree.tree_card_data import TreeCardData


class TreeCard:
    def __init__(self: 'TreeCard', habitat: Habitat, scientific_name: str, common_name: str,
                 points: int, height: int, nutrients: Nutrients, michigander: bool) -> None:
        self.habitat: Final[Habitat] = habitat
        self.scientific_name: Final[str] = scientific_name
        self.common_name: Final[str] = common_name
        self.points: Final[int] = points
        self.height: Final[int] = height
        self.nutrients: Final[Nutrients] = nutrients
        self.michigander: Final[bool] = michigander

    @staticmethod
    def from_card_data(card_data: TreeCardData) -> 'TreeCard':
        habitat = Habitat.from_string(card_data.habitat)
        nutrients = Nutrients.from_tree_card_data(card_data)
        michigander = True if (card_data.michigander == 1) else False

        return TreeCard(habitat, card_data.scientific_name, card_data.common_name,
                        card_data.points, card_data.height, nutrients, michigander)

    def to_string(self: 'TreeCard') -> str:
        return '{} | ({} pts, {} ft, {}) | needs {}'.format(
            self.common_name,
            self.points,
            self.height,
            self.habitat.value,
            self.nutrients.to_string(),
        )

    def to_short_string(self: 'TreeCard') -> str:
        return '{} | ({} pts, {} ft)'.format(self.common_name, self.points, self.height)

    # def info(self: 'TreeCard') -> str:
    #     return '{} is a {}.'.format(self.scientific_name, self.habitat.value)
    #
    # def plant_facts(self): # returns a list of everything to be added to database
    #     return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]


if __name__ == '__main__':
    tree_data = TreeCardData('Conifer', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1)
    tree_card = TreeCard.from_card_data(tree_data)
    print(tree_card.to_string())
    print(tree_card.to_short_string())
