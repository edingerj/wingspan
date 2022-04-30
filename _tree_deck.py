"""
Dependencies: pandas
"""

from random import shuffle
from typing import List, Dict

from pandas import read_csv

from _tree import Tree


class TreeDeck:
    def __init__(self):
        self.cards: List[Tree] = TreeDeck._import_from_csv()
        shuffle(self.cards)

    @staticmethod
    def _import_from_csv() -> List['Tree']:
        df = read_csv("data/trees.csv")
        trees = df.values.tolist()
        return list(map(lambda tree: Tree(*tree), trees))

    def draw_card(self) -> Tree:
        return self.cards.pop()


tree_deck = TreeDeck()

if __name__ == '__main__':
    tree_name_lengths: Dict[int, Tree] = {len(tree.common_name): tree for tree in tree_deck.cards}
    longest_name_length: int = max(tree_name_lengths.keys())

    print('Total Trees: {}'.format(len(tree_deck.cards)))
    print('Longest Tree Name: {}, {} characters'.format(
        tree_name_lengths[longest_name_length].common_name,
        longest_name_length,
    ))
    print('Random Card: {}'.format(tree_deck.draw_card().common_name))
