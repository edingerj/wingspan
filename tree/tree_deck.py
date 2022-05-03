"""
Dependencies: pandas
"""

from random import shuffle
from typing import List, Dict, Final, Union

from pandas import read_csv

from tree_card import TreeCard
from tree_card_data import TreeCardData


class TreeDeck:
    def __init__(self: 'TreeDeck', cards: List[TreeCard]):
        self.cards: Final[List[TreeCard]] = cards
        shuffle(self.cards)

    @staticmethod
    def from_csv() -> 'TreeDeck':
        card_rows: Final[List[Union[str, int]]] = read_csv('data/trees.csv').values.tolist()
        card_datum: Final[List[TreeCardData]] = list(map(lambda card_row: TreeCardData(*card_row), card_rows))
        cards: Final[List[TreeCard]] = list(map(lambda card_data: TreeCard.from_card_data(card_data), card_datum))
        return TreeDeck(cards)

    def draw_card(self: 'TreeDeck') -> TreeCard:
        return self.cards.pop()


if __name__ == '__main__':
    tree_deck = TreeDeck.from_csv()
    tree_name_lengths: Dict[int, TreeCard] = {len(tree.common_name): tree for tree in tree_deck.cards}
    longest_name_length: int = max(tree_name_lengths.keys())

    print('Total Trees: {}'.format(len(tree_deck.cards)))
    print('Longest Tree Name: {}, {} characters'.format(
        tree_name_lengths[longest_name_length].common_name,
        longest_name_length,
    ))
    print('Random Card: {}'.format(tree_deck.draw_card().common_name))
