from typing import Final

from tree.habitat import Habitat
from tree.nutrients import Nutrients
from tree.tree_card_data import TreeCardData
from util.ansi import AnsiFormat, AnsiColor, visible_offset
from util.border import BorderBox
from util.table import delimiter


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

    def card_format(self: 'TreeCard', card_color=AnsiColor.BRIGHT_BLACK) -> str:
        regions = [[
            '{} {}'.format(
                self.common_name,
                AnsiFormat.italic('({})'.format(self.scientific_name)),
            ),
            self.nutrients.emoji_format().ljust(15 - visible_offset(self.nutrients.emoji_format())),
        ], [
            self.habitat.to_string(),
            '{} {}'.format(self.points, 'pts' if self.points != 1 else 'pt').ljust(6),
            '{} ft'.format(self.height).ljust(6),
        ]]
        if self.michigander:
            regions.insert(1, '{} is native to Michigan.'.format(self.common_name))
        return BorderBox.of(regions, card_color).draw()

    def table_format(self: 'TreeCard', delimiter_color=AnsiColor.DEFAULT) -> str:
        return '{1} {0} {2} {0} {3} {0} {4} {0} {5}'.format(
            delimiter(delimiter_color),
            self.common_name.ljust(24),
            '{} {}'.format(self.points, 'pts' if self.points != 1 else 'pt').ljust(6),
            '{} ft'.format(self.height).ljust(6),
            '{}'.format(self.habitat.to_string()).ljust(10),
            self.nutrients.emoji_format(),
        )

    def arboretum_format(self: 'TreeCard', delimiter_color=AnsiColor.DEFAULT) -> str:
        return '{1} {0} {2} {0} {3}'.format(
            delimiter(delimiter_color),
            self.common_name.ljust(24),
            '{} {}'.format(self.points, 'pts' if self.points != 1 else 'pt').ljust(6),
            '{} ft'.format(self.height),
        )

    # def info(self: 'TreeCard') -> str:
    #     return '{} is a {}.'.format(self.scientific_name, self.habitat.to_string())
    #
    # def plant_facts(self): # returns a list of everything to be added to database
    #     return [self.family, self.genus_species, self.common_name, self.physiognomy, self.conservatism, self.wetness]


if __name__ == '__main__':
    tree_data1 = TreeCardData('CONIFEROUS', 'Abies balsamea', 'balsam fir', 3, 90, 1, 0, 0, 0, 1)
    tree_data2 = TreeCardData('CONIFEROUS', 'Sequoia sempervirens', 'redwood', 10, 380, 1, 1, 1, 1, 0)
    tree_card1 = TreeCard.from_card_data(tree_data1)
    tree_card2 = TreeCard.from_card_data(tree_data2)

    print(tree_card1.card_format())
    print(tree_card2.card_format())

    print(tree_card1.table_format())
    print(tree_card1.arboretum_format())
