from typing import Iterable, List, Optional

from tree import TreeCard, tree_deck


class Hand(List[TreeCard]):
    def __init__(self: 'Hand', tree_cards: Iterable[TreeCard] = ()) -> None:
        super(Hand, self).__init__(tree_cards)

    @staticmethod
    def from_deck(size: int = 3) -> 'Hand':
        tree_cards = [tree_deck.draw_card() for _ in range(size)]
        return Hand(tree_cards)

    # return: the drawn tree card
    def draw_from_deck(self: 'Hand') -> TreeCard:
        tree_card = tree_deck.draw_card()
        self.append(tree_card)
        return tree_card

    # return: the drawn tree card
    def draw_from_display(self: 'Hand', tree_card: TreeCard) -> TreeCard:
        self.append(tree_card)
        return tree_card

    def has_cards(self: 'Hand') -> bool:
        return len(self) > 0

    # where choice can be a tree common name, or a 1 index
    def index_of(self: 'Hand', choice: str, include_random: bool = False) -> Optional[int]:
        tree_card: Optional[TreeCard] = \
            next(filter(lambda card: card.common_name.lower() == choice.lower(), self), None)
        if tree_card is not None:
            return self.index(tree_card)
        try:
            index = int(choice) - 1
            length = len(self) + 1 if include_random else len(self)
            return index if (index < length) else None
        except ValueError:
            return None

    def to_string(self: 'Hand') -> str:
        return '\n'.join([
            '  {}. {}'.format(index + 1, tree_card.to_string())
            for index, tree_card in enumerate(self)
        ])


if __name__ == '__main__':
    hand = Hand.from_deck()
    print(hand.to_string())
