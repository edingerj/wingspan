from typing import Iterable, List

from tree import TreeCard, tree_deck


class Hand(List[TreeCard]):
    def __init__(self: 'Hand', tree_cards: Iterable = ()) -> None:
        super(Hand, self).__init__(tree_cards)

    @staticmethod
    def from_deck(size: int = 3) -> 'Hand':
        tree_cards = [tree_deck.draw_card() for i in range(size)]
        return Hand(tree_cards)

    def has_cards(self: 'Hand') -> bool:
        return len(self) > 0

    def to_string(self: 'Hand') -> str:
        result = ''
        for index, tree_card in enumerate(self):
            result += '  {}. {}\n'.format(index + 1, tree_card.to_string())
        return result.rstrip()


if __name__ == '__main__':
    hand = Hand.from_deck()
    print(hand.to_string())
