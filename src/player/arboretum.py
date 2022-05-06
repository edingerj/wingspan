from functools import reduce
from operator import add
from typing import Dict, List

from tree import Habitat, TreeCard


class Arboretum(Dict[Habitat, List[TreeCard]]):
    def __init__(self: 'Arboretum') -> None:
        super(Arboretum, self).__init__({
            habitat: [] for habitat in Habitat
        })

    def plant_tree(self: 'Arboretum', tree_card: TreeCard) -> None:
        self[tree_card.habitat].append(tree_card)

    def get_all_trees(self: 'Arboretum') -> List[TreeCard]:
        return reduce(add, [self[habitat] for habitat in Habitat])

    def has_trees(self: 'Arboretum') -> bool:
        return len(self.get_all_trees()) > 0

    def get_total_points(self: 'Arboretum') -> int:
        return sum([tree_card.points for tree_card in self.get_all_trees()])

    def get_total_height(self: 'Arboretum') -> int:
        return sum([tree_card.height for tree_card in self.get_all_trees()])

    def get_populated_habitats(self: 'Arboretum') -> List[Habitat]:
        return list(filter(lambda habitat: len(self[habitat]) > 0, self.keys()))

    def __str__(self: 'Arboretum') -> str:
        return '\n'.join(self.get_habitat_string(habitat) for habitat in self.get_populated_habitats())

    def get_habitat_string(self: 'Arboretum', habitat: Habitat) -> str:
        return '  {} Habitat:\n'.format(habitat.value) + \
               '\n'.join(
                   '    {}. {}'.format(index + 1, tree_card.str_short())
                   for index, tree_card in enumerate(self[habitat])
               )


if __name__ == '__main__':
    arb = Arboretum()
    arb.plant_tree(TreeCard(Habitat.CONIFER, 'Abies balsamea', 'balsam fir', 3, 90, [], True))
    arb.plant_tree(TreeCard(Habitat.DECIDUOUS, 'Acer negundo', 'boxelder', 0, 70, [], True))

    print('Arboretum:')
    print(arb)
    print('Total Points: {}'.format(arb.get_total_points()))
    print('Total Height: {}'.format(arb.get_total_height()))
