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
        card_data: Final[List[TreeCardData]] = list(map(TreeCardData.of, read_csv('data/trees.csv').values))
        tree_cards: Final[List[TreeCard]] = list(map(TreeCard.from_card_data, card_data))
        return TreeDeck(tree_cards)

    def draw_card(self: 'TreeDeck') -> TreeCard:
        return self.pop()

    def to_string(self: 'TreeDeck') -> str:
        return '\n'.join([
            '{}. {}'.format(index + 1, tree_card.to_string())
            for index, tree_card in enumerate(self)
        ])


if __name__ == '__main__':
    tree_deck = TreeDeck.from_csv()
    tree_name_lengths: Dict[int, TreeCard] = {len(tree.common_name): tree for tree in tree_deck}
    longest_name_length: int = max(tree_name_lengths.keys())

    print('Total Trees: {}'.format(len(tree_deck)))
    print(tree_deck.to_string())

    print('\nLongest Tree Name: {}, {} characters'.format(
        tree_name_lengths[longest_name_length].common_name, longest_name_length))
    print('Random Card: {}'.format(tree_deck.draw_card().common_name))
