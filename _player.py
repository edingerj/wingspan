from typing import List, Optional

from _bonus_card import all_bonus_cards, BonusCard
from _nutrient import Nutrient
from _tree import Tree
from _tree_deck import tree_deck


class Player:
    # make the computer another instance of Player
    def __init__(self, number=None, name=None) -> None:
        self.number = number
        self.name = name
        self.nutrients: List[Nutrient] = []
        self.tree_cards: List[Tree] = []
        self.Conifer: List[Tree] = []
        self.Deciduous: List[Tree] = []
        self.Urban: List[Tree] = []
        self.hugs = 0
        self.tree_points = 0
        self.combined_height = 0
        self.bonus: Optional[BonusCard] = None
        self.bonus_points = 0
        # self.scores = []

    # player is given 1 bonus card randomly (need to implement choice of bonus cards)
    def assign_bonus_cards(self) -> None:
        self.bonus = all_bonus_cards.pop()

    def draw_tree_card(self) -> None:
        tree_card = tree_deck.draw_card()
        self.tree_cards.append(tree_card)

    def remove_nutrients(self, nutrients: List[Nutrient]) -> None:
        for nutrient in nutrients:
            self.nutrients.remove(nutrient)
