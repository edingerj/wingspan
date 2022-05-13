from typing import Final, List

from bonus import BonusCard, BonusToken
from player.arboretum import Arboretum
from player.hand import Hand
from player.player_color import PlayerColor
from player.player_name import PlayerName
from tree import Habitat, Nutrients, TreeCard
from util.ansi import AnsiColor
from util.border import BorderBox


class Player:
    def __init__(self: 'Player', name: PlayerName, color: PlayerColor, bonus_class: BonusCard) -> None:
        self.name: Final[PlayerName] = name
        self.color: Final[PlayerColor] = color
        self.bonus_class: Final[BonusCard] = bonus_class
        self.nutrients: Final[Nutrients] = Nutrients.random_sorted()
        self.hand: Final[Hand] = Hand.from_deck()
        self.arboretum: Final[Arboretum] = Arboretum()
        self.bonuses: Final[List[BonusToken]] = []
        self.hugs: int = 0

    # return: the drawn tree card
    def draw_tree_card_from_deck(self: 'Player') -> TreeCard:
        return self.hand.draw_from_deck()

    # return: the drawn tree card
    def draw_tree_card_from_display(self: 'Player', tree_card: TreeCard) -> TreeCard:
        return self.hand.draw_from_display(tree_card)

    # gain 1 additional nutrient card for every Coniferous tree in arb
    # return: the drawn nutrients
    def draw_nutrient_cards(self: 'Player') -> Nutrients:
        total_coniferous = len(self.arboretum[Habitat.CONIFEROUS])
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

    def overview_format(self: 'Player', card_color=AnsiColor.BRIGHT_BLACK) -> str:
        regions = []
        if self.arboretum.has_trees():
            regions.append('{}\n{}'.format(
                self.color.ansi().foreground('{}\'s Arboretum:'.format(self.name)),
                '{}'.format(self.arboretum.table_format(card_color)),
            ))
        if self.hand.has_cards():
            regions.append('{}\n{}'.format(
                self.color.ansi().foreground('{}\'s Hand:'.format(self.name)),
                '{}'.format(self.hand.table_format(card_color)),
            ))
        if len(self.nutrients) > 0:
            regions.append('{}\n{}'.format(
                self.color.ansi().foreground('{}\'s Nutrients:'.format(self.name)),
                '  {}'.format(self.nutrients.emoji_format()),
            ))
        if self.bonus_class is not None:
            regions.append('{}{}\n{}'.format(
                self.color.ansi().foreground('{}\'s Bonus:'.format(self.name)),
                ' {}'.format(self.bonus_class.name),
                '  {}'.format(self.bonus_class.description),
            ))
        return BorderBox.of(regions, card_color).draw()

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
    player = Player('Seb', PlayerColor.BLUE, BonusCard('Michigander', '', None, True))
    player.draw_tree_card_from_deck()

    print('Player: {}'.format(player.name))
    print(player.overview_format())

    can_plant_tree = player.can_plant_tree(player.hand[0])
    print('Can plant {}? {}'.format(player.hand[0].common_name, can_plant_tree))
