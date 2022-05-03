from typing import List

from nutrient import Nutrient
from tree_card_data import TreeCardData


class TreeCard:
    def __init__(self: 'TreeCard', habitat: str, scientific_name: str, common_name: str,
                 points: int, height: int, nutrients: List[Nutrient], michigander: bool) -> None:
        self.habitat: str = habitat
        self.scientific_name: str = scientific_name
        self.common_name: str = common_name
        self.points: int = points
        self.height: int = height
        self.nutrients: List[Nutrient] = nutrients
        self.hugs: int = 0
        self.michigander: bool = michigander

    @staticmethod
    def from_card_data(tree_card_data: TreeCardData) -> 'TreeCard':
        nutrients: List[Nutrient] = Nutrient.list_from_tree_card_data(tree_card_data)
        michigander = True if (tree_card_data.michigander == 1) else False

        return TreeCard(tree_card_data.habitat, tree_card_data.scientific_name, tree_card_data.common_name,
                        tree_card_data.points, tree_card_data.height, nutrients, michigander)

    def info(self: 'TreeCard') -> str:
        return self.scientific_name + ' is a ' + self.habitat + '.'

    def get_formatted_info(self: 'TreeCard') -> str:
        return '- {} | ({} pts, {} ft, {}) | requires {}'.format(
            self.common_name,
            self.points,
            self.height,
            self.habitat,
            list(map(lambda nutrient: nutrient.value, self.nutrients)),
        )

    # def plant_facts(self): # returns a list of everything to be added to database
    #     return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]


if __name__ == '__main__':
    tree_data = TreeCardData('Conifer', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1)
    tree_card = TreeCard.from_card_data(tree_data)
    print(tree_card.get_formatted_info())
