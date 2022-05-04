from functools import reduce
from operator import concat
from typing import List, Dict

from tree import Habitat, TreeCard


class Arboretum(Dict[Habitat, List[TreeCard]]):
    def __init__(self: 'Arboretum') -> None:
        super(Arboretum, self).__init__({
            habitat: [] for habitat in Habitat
        })

    def get_all_trees(self: 'Arboretum') -> List[TreeCard]:
        return reduce(concat, [self[habitat] for habitat in Habitat])

    def has_trees(self: 'Arboretum') -> bool:
        return len(self.get_all_trees()) > 0

    def get_combined_height(self: 'Arboretum') -> int:
        return sum(map(lambda tree_card: tree_card.height, self.get_all_trees()))

    def plant_tree(self: 'Arboretum', tree_card: TreeCard) -> None:
        self[tree_card.habitat].append(tree_card)

    def to_string(self: 'Arboretum') -> str:
        result: str = ''
        for habitat in self.keys():
            if len(self[habitat]) > 0:
                result += '  {}: {}\n'.format(habitat.value, list(map(TreeCard.get_name, self[habitat])))
        return result.rstrip()


if __name__ == '__main__':
    arb = Arboretum()
    arb.plant_tree(TreeCard(Habitat.CONIFER, 'Abies balsamea', 'balsam fir', 3, 90, [], True))
    arb.plant_tree(TreeCard(Habitat.DECIDUOUS, 'Acer negundo', 'boxelder', 0, 70, [], True))

    print('Arboretum:')
    print(arb.to_string())
    print('Combined Height: {}'.format(arb.get_combined_height()))
