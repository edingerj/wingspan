from typing import Final, Optional

from bonus import all_bonus_cards, BonusCard
from player.arboretum import Arboretum
from player.hand import Hand
from tree import Habitat, Nutrients, TreeCard


class Player:
    def __init__(self: 'Player', name: str) -> None:
        self.name: Final[str] = name
        self.nutrients: Final[Nutrients] = Nutrients.random_sorted()
        self.hand: Final[Hand] = Hand.from_deck()
        self.arboretum: Final[Arboretum] = Arboretum()
        self.bonus: Optional[BonusCard] = None
        self.hugs: int = 0
        self.tree_points: int = 0
        self.combined_height: int = 0
        self.bonus_points: int = 0

    # player is given 1 bonus card randomly
    # Todo: implement choice of bonus cards
    def assign_bonus_card(self: 'Player') -> None:
        self.bonus = all_bonus_cards.pop()

    # return: the drawn tree card
    def draw_tree_card(self: 'Player') -> TreeCard:
        return self.hand.draw_from_deck()

    # gain 1 additional nutrient card for every Conifer in arb
    # return: the drawn nutrients
    def draw_nutrient_cards(self: 'Player') -> Nutrients:
        total_coniferous = len(self.arboretum[Habitat.CONIFER])
        nutrients = Nutrients.random(total_coniferous + 1)
        self.nutrients.extend(nutrients)
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
            result += '  {}\n'.format(self.nutrients.to_string())
            result += '{}\n'.format(75 * '_')
        result += '{}\'s Bonus: {}\n'.format(self.name, self.bonus.name)
        result += '  {}\n'.format(self.bonus.description)
        result += '{}<\n'.format(37 * '<>')
        return result

    def get_total_score(self: 'Player', has_tallest_arboretum: bool) -> int:
        self.evaluate_points(has_tallest_arboretum)
        return sum([self.hugs, self.tree_points, self.bonus_points])

    def evaluate_points(self: 'Player', has_tallest_arboretum: bool) -> None:
        self.tree_points = self.arboretum.get_total_points()
        self.bonus_points = self.get_bonus_points(has_tallest_arboretum)

    def get_bonus_points(self: 'Player', has_tallest_arboretum: bool) -> int:
        bonus_points: int = 0
        # get 2 bonus points for each michigander card in arb
        if self.bonus.name == 'michigander':
            for tree in self.arboretum.get_all_trees():
                if tree.michigander:
                    bonus_points += 2
        # get 10 bonus point if you have the tallest combined height
        elif self.bonus.name == 'tree climber':
            if has_tallest_arboretum:
                bonus_points += 10
        # anyone can get 10 bonus points for having highest combined height, like longest roads in Catan
        if has_tallest_arboretum:
            bonus_points += 10
        return bonus_points


if __name__ == '__main__':
    player = Player('Seb')
    player.assign_bonus_card()
    player.draw_tree_card()

    print('Player: {}'.format(player.name))
    print(player.to_string())

    can_plant_tree = player.can_plant_tree(player.hand[0])
    print('Can plant {}? {}'.format(player.hand[0].common_name, can_plant_tree))
