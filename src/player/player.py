from typing import Final, List

from bonus import BonusClass, BonusCard
from player.arboretum import Arboretum
from player.hand import Hand
from tree import Habitat, Nutrients, TreeCard


class Player:
    def __init__(self: 'Player', name: str, bonus_class: BonusClass) -> None:
        self.name: Final[str] = name
        self.bonus_class: Final[BonusClass] = bonus_class
        self.nutrients: Final[Nutrients] = Nutrients.random_sorted()
        self.hand: Final[Hand] = Hand.from_deck()
        self.arboretum: Final[Arboretum] = Arboretum()
        self.bonuses: Final[List[BonusCard]] = []
        self.hugs: int = 0

    # return: the drawn tree card
    def draw_tree_card_from_deck(self: 'Player') -> TreeCard:
        return self.hand.draw_from_deck()

    # return: the drawn tree card
    def draw_tree_card_from_display(self: 'Player', tree_card: TreeCard) -> TreeCard:
        return self.hand.draw_from_display(tree_card)

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
        result += '{}\'s Bonus: {}\n'.format(self.name, self.bonus_class.name)
        result += '  {}\n'.format(self.bonus_class.description)
        result += '{}<\n'.format(37 * '<>')
        return result

    def get_total_score(self: 'Player') -> int:
        return sum([
            self.hugs,
            self.get_total_tree_points(),
            self.get_total_bonus_points(),
        ])

    def get_total_tree_points(self: 'Player') -> int:
        return self.arboretum.get_total_points()

    def get_total_bonus_points(self: 'Player') -> int:
        return self.bonus_class.count_bonus_points(self.bonuses, self.arboretum.get_all_trees())


if __name__ == '__main__':
    player = Player('Seb', BonusClass('Michigander', '', None, True))
    player.draw_tree_card()

    print('Player: {}'.format(player.name))
    print(player.to_string())

    can_plant_tree = player.can_plant_tree(player.hand[0])
    print('Can plant {}? {}'.format(player.hand[0].common_name, can_plant_tree))
