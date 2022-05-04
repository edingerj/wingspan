from itertools import accumulate
from typing import List, Final

from tree import Habitat, TreeCard


class Arboretum(dict):
    def __init__(self: 'Arboretum') -> None:
        super().__init__()
        self[Habitat.CONIFER]: Final[List[TreeCard]] = []
        self[Habitat.DECIDUOUS]: Final[List[TreeCard]] = []
        self[Habitat.URBAN]: Final[List[TreeCard]] = []

    def get_all_trees(self: 'Arboretum') -> List[TreeCard]:
        return [
            *self[Habitat.CONIFER],
            *self[Habitat.DECIDUOUS],
            *self[Habitat.URBAN],
        ]

    def has_trees(self: 'Arboretum') -> bool:
        return len(self.get_all_trees()) > 0

    def get_combined_height(self: 'Arboretum') -> int:
        return max(accumulate(map(lambda tree_card: tree_card.height, self.get_all_trees())))

    def plant_tree(self: 'Arboretum', tree_card: TreeCard) -> None:
        self[tree_card.habitat].append(tree_card)

    def to_string(self: 'Arboretum') -> str:
        result: str = ''
        for habitat in self.keys():
            if len(self[habitat]) > 0:
                result += '{}: {}\n'.format(habitat.value, list(map(TreeCard.get_name, self[habitat])))
        return result.strip()


if __name__ == '__main__':
    arb = Arboretum()
    arb.plant_tree(TreeCard(Habitat.CONIFER, 'Abies balsamea', 'balsam fir', 3, 90, [], True))
    arb.plant_tree(TreeCard(Habitat.DECIDUOUS, 'Acer negundo', 'boxelder', 0, 70, [], True))

    print('Arboretum:')
    print(arb.to_string())
    print('Combined Height: {}'.format(arb.get_combined_height()))
