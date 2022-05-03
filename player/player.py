from typing import List, Optional

from bonus import all_bonus_cards, BonusCard
from tree import Nutrient, TreeCard, tree_deck


class Player:
    # make the computer another instance of Player
    def __init__(self: 'Player', player_id: Optional[int] = None, name: Optional[str] = None) -> None:
        self.player_id: Optional[int] = player_id
        self.name: Optional[str] = name
        self.nutrients: List[Nutrient] = []
        self.hand: List[TreeCard] = []
        self.Conifer: List[TreeCard] = []
        self.Deciduous: List[TreeCard] = []
        self.Urban: List[TreeCard] = []
        self.hugs: int = 0
        self.tree_points: int = 0
        self.combined_height: int = 0
        self.bonus: Optional[BonusCard] = None
        self.bonus_points: int = 0
        # self.scores = []

    # player is given 1 bonus card randomly (need to implement choice of bonus cards)
    def assign_bonus_cards(self) -> None:
        self.bonus = all_bonus_cards.pop()

    def draw_tree_card(self) -> None:
        tree_card = tree_deck.draw_card()
        self.hand.append(tree_card)

    def remove_nutrients(self, nutrients: List[Nutrient]) -> None:
        for nutrient in nutrients:
            self.nutrients.remove(nutrient)
