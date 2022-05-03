from typing import List

from tree.nutrient import Nutrient
from tree.tree_card_def import TreeCardDef


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
    def from_card_def(tree_card_def: TreeCardDef) -> 'TreeCard':
        nutrients: List[Nutrient] = Nutrient.list_from_tree_card_def(tree_card_def)
        michigander = True if (tree_card_def.michigander == 1) else False

        return TreeCard(tree_card_def.habitat, tree_card_def.scientific_name, tree_card_def.common_name,
                        tree_card_def.points, tree_card_def.height, nutrients, michigander)

    def info(self):
        return self.scientific_name + ' is a ' + self.habitat + '.'

    def get_formatted_info(self):
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
    tree_def = TreeCardDef('Conifer', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1)
    tree_card = TreeCard.from_card_def(tree_def)
    print(tree_card.get_formatted_info())
