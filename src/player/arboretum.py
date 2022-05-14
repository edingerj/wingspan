from functools import reduce
from operator import add
from typing import Dict, List

from tree import Habitat, TreeCard
from util.ansi import AnsiColor


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

    def table_format(self: 'Arboretum', header_color=AnsiColor.DEFAULT, delimiter_color=AnsiColor.DEFAULT) -> str:
        return '\n'.join(
            self.table_format_habitat(habitat, header_color, delimiter_color)
            for habitat in self.get_populated_habitats()
        )

    def table_format_habitat(self: 'Arboretum', habitat: Habitat,
                             header_color=AnsiColor.DEFAULT, delimiter_color=AnsiColor.DEFAULT) -> str:
        return '  {}\n{}'.format(
            header_color.foreground('{} Habitat:'.format(habitat.to_string())),
            '\n'.join('  {} {}'.format(
                '{}.'.format(index + 1).ljust(3),
                tree_card.arboretum_format(delimiter_color),
            ) for index, tree_card in enumerate(self[habitat]))
        )


if __name__ == '__main__':
    arb = Arboretum()
    arb.plant_tree(TreeCard(Habitat.CONIFEROUS, 'Abies balsamea', 'balsam fir', 3, 90, [], True))
    arb.plant_tree(TreeCard(Habitat.DECIDUOUS, 'Acer negundo', 'boxelder', 0, 70, [], True))

    print('Arboretum:')
    print(arb.table_format())
    print('Total Points: {}'.format(arb.get_total_points()))
    print('Total Height: {}'.format(arb.get_total_height()))
