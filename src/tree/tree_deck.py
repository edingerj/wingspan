"""
Dependencies: pandas
"""

from random import shuffle
from typing import Dict, Final, Iterable, List

from pandas import read_csv

from tree.tree_card import TreeCard
from tree.tree_card_data import TreeCardData


class TreeDeck(List[TreeCard]):
    def __init__(self: 'TreeDeck', tree_cards: Iterable[TreeCard] = ()):
        super(TreeDeck, self).__init__(tree_cards)
        shuffle(self)

    @staticmethod
    def from_csv() -> 'TreeDeck':
        # Todo: Title Case tree names
        #  both common_name and scientific_name
        card_data: Final[List[TreeCardData]] = list(map(TreeCardData.of, read_csv('data/trees.csv').values))
        tree_cards: Final[List[TreeCard]] = list(map(TreeCard.from_card_data, card_data))
        return TreeDeck(tree_cards)

    # Todo: handle case of empty deck
    def draw_card(self: 'TreeDeck') -> TreeCard:
        return self.pop()

    def __str__(self: 'TreeDeck') -> str:
        return self.get_header_rows() + '\n'.join([
            '{} {}'.format(
                '{}.'.format(index + 1).ljust(3),
                tree_card
            ) for index, tree_card in enumerate(self)
        ])

    @staticmethod
    def get_header_rows() -> str:
        return '    Common Name              │ Points │ Height │ Habitat   │ Nutrients\n' + \
               '─────────────────────────────┼────────┼────────┼───────────┼───────────\n'


if __name__ == '__main__':
    tree_deck = TreeDeck.from_csv()
    tree_name_lengths: Dict[int, TreeCard] = {len(tree.common_name): tree for tree in tree_deck}
    longest_name_length: int = max(tree_name_lengths.keys())

    print(tree_deck)

    print('\nLongest Tree Name: {}, {} characters'.format(
        tree_name_lengths[longest_name_length].common_name, longest_name_length))
    print('Random Card: {}'.format(tree_deck.draw_card().common_name))
