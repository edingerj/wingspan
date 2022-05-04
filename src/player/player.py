from typing import Final, List, Optional

from bonus import all_bonus_cards, BonusCard
from player.arboretum import Arboretum
from player.hand import Hand
from tree import Habitat, Nutrient, TreeCard, tree_deck


class Player:
    # make the computer another instance of Player
    def __init__(self: 'Player', player_id: Optional[int] = None, name: Optional[str] = None) -> None:
        self.player_id: Final[Optional[int]] = player_id
        self.name: Final[Optional[str]] = name
        self.nutrients: List[Nutrient] = []
        self.hand: Final[Hand] = Hand.from_deck()
        self.arboretum: Final[Arboretum] = Arboretum()
        self.bonus: Optional[BonusCard] = None
        self.hugs: int = 0
        self.tree_points: int = 0
        self.combined_height: int = 0
        self.bonus_points: int = 0
        # self.scores = []

    # player is given 1 bonus card randomly
    # Todo: implement choice of bonus cards
    def assign_bonus_card(self: 'Player') -> None:
        self.bonus = all_bonus_cards.pop()

    # return: the drawn tree card
    def draw_tree_card(self: 'Player') -> TreeCard:
        tree_card = tree_deck.draw_card()
        self.hand.append(tree_card)
        return tree_card

    # gain 1 additional nutrient card for every Conifer in arb
    # return: the drawn nutrients
    def draw_nutrient_cards(self: 'Player', draw: int = 1) -> List[Nutrient]:
        total_coniferous = len(self.arboretum[Habitat.CONIFER])
        nutrients = [Nutrient.random() for i in range(draw + total_coniferous)]
        self.nutrients.extend(nutrients)
        self.nutrients.sort()
        return nutrients

    def can_plant_tree(self: 'Player', tree_card: TreeCard) -> bool:
        if tree_card not in self.hand:
            return False
        available_nutrients = self.nutrients.copy()
        for nutrient in tree_card.nutrients:
            if nutrient in available_nutrients:
                available_nutrients.remove(nutrient)
            else:
                return False
        return True

    def plant_tree(self: 'Player', tree_card: TreeCard) -> None:
        self.hand.remove(tree_card)
        for nutrient in tree_card.nutrients:
            self.nutrients.remove(nutrient)
        self.arboretum.plant_tree(tree_card)
        self.combined_height = self.arboretum.get_total_height()

    # hug 1 additional tree for each Deciduous tree in arb
    # return: the number of trees newly hugged
    def hug_trees(self: 'Player') -> int:
        total_deciduous = len(self.arboretum[Habitat.DECIDUOUS])
        self.hugs += total_deciduous + 1
        return total_deciduous + 1

    def to_string(self: 'Player') -> str:
        result = '{}<\n'.format(37 * '<>')
        if self.arboretum.has_trees():
            result += '{}\'s Arboretum:\n'.format(self.name)
            result += '{}\n'.format(self.arboretum.to_string())
            result += '{}\n'.format(75 * '_')
        if self.hand.has_cards():
            result += '{}\'s Hand:\n'.format(self.name)
            result += '{}\n'.format(self.hand.to_string())
            result += '{}\n'.format(75 * '_')
        if len(self.nutrients) > 0:
            result += '{}\'s Nutrients:\n'.format(self.name)
            result += '  {}\n'.format(' '.join([nutrient.to_emoji() for nutrient in self.nutrients]))
            result += '{}\n'.format(75 * '_')
        result += '{}\'s Bonus: {}\n'.format(self.name, self.bonus.name)
        result += '  {}\n'.format(self.bonus.description)
        result += '{}<\n'.format(37 * '<>')
        return result


if __name__ == '__main__':
    player = Player(1, 'Seb')
    player.assign_bonus_card()
    player.draw_tree_card()

    print('Player: {}'.format(player.name))
    print(player.to_string())

    can_plant_tree = player.can_plant_tree(player.hand[0])
    print('Can plant {}? {}'.format(player.hand[0].common_name, can_plant_tree))
