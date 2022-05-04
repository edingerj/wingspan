from typing import List, Final

from tree.habitat import Habitat
from tree.nutrient import Nutrient
from tree.tree_card_data import TreeCardData


class TreeCard:
    def __init__(self: 'TreeCard', habitat: Habitat, scientific_name: str, common_name: str,
                 points: int, height: int, nutrients: List[Nutrient], michigander: bool) -> None:
        self.habitat: Final[Habitat] = habitat
        self.scientific_name: Final[str] = scientific_name
        self.common_name: Final[str] = common_name
        self.points: Final[int] = points
        self.height: Final[int] = height
        self.nutrients: Final[List[Nutrient]] = nutrients
        self.michigander: Final[bool] = michigander
        self.hugs: int = 0

    @staticmethod
    def from_card_data(card_data: TreeCardData) -> 'TreeCard':
        habitat = Habitat.from_string(card_data.habitat)
        nutrients = Nutrient.list_from_tree_card_data(card_data)
        michigander = True if (card_data.michigander == 1) else False

        return TreeCard(habitat, card_data.scientific_name, card_data.common_name,
                        card_data.points, card_data.height, nutrients, michigander)

    def info(self: 'TreeCard') -> str:
        return '{} is a {}.'.format(self.scientific_name, self.habitat.value)

    def to_string(self: 'TreeCard') -> str:
        return '{} | ({} pts, {} ft, {}) | requires {}'.format(
            self.common_name,
            self.points,
            self.height,
            self.habitat.value,
            list(map(lambda nutrient: nutrient.value, self.nutrients)),
        )

    def get_name(self: 'TreeCard') -> str:
        return self.common_name

    # def plant_facts(self): # returns a list of everything to be added to database
    #     return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]


if __name__ == '__main__':
    tree_data = TreeCardData('Conifer', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1)
    tree_card = TreeCard.from_card_data(tree_data)
    print(tree_card.to_string())
    print(tree_card.info())
