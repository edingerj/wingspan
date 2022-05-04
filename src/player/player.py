from typing import Final, List, Optional

from bonus import all_bonus_cards, BonusCard
from gameplay import sleep
from player.arboretum import Arboretum
from player.hand import Hand
from tree import Habitat, Nutrient, TreeCard, tree_deck


class Player:
    # make the computer another instance of Player
    def __init__(self: 'Player', player_id: Optional[int] = None, name: Optional[str] = None) -> None:
        self.player_id: Optional[int] = player_id
        self.name: Optional[str] = name
        self.nutrients: List[Nutrient] = []
        self.hand: Final[Hand] = Hand.from_deck()
        self.arboretum: Final[Arboretum] = Arboretum()
        self.hugs: int = 0
        self.tree_points: int = 0
        self.combined_height: int = 0
        self.bonus: Optional[BonusCard] = None
        self.bonus_points: int = 0
        # self.scores = []

    # player is given 1 bonus card randomly
    # Todo: implement choice of bonus cards
    def assign_bonus_card(self: 'Player') -> None:
        self.bonus = all_bonus_cards.pop()

    def draw_tree_card(self: 'Player') -> None:
        tree_card = tree_deck.draw_card()
        self.hand.append(tree_card)

    # gain 1 additional nutrient card for every Conifer in arb
    def draw_nutrient_cards(self: 'Player', draw: int = 1) -> None:
        sleep(0.2)
        print('*** rolling dice ***')
        total_coniferous = len(self.arboretum[Habitat.CONIFER])
        for i in range(draw + total_coniferous):
            nutrient = Nutrient.random()
            self.nutrients.append(nutrient)
            print('  {0} rolled a {1}! Adding it to {0}\'s pile of nutrients...'.format(self.name, nutrient.value))
            sleep(0.3)

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
        self.combined_height = self.arboretum.get_combined_height()
        print('Planting a ' + tree_card.common_name + '...')
        sleep(0.5)
        print('Your combined height is: {}'.format(self.combined_height))
        sleep(0.5)

    # hug 1 additional tree for each Deciduous tree in arb
    def hug_trees(self: 'Player') -> None:
        total_deciduous = len(self.arboretum[Habitat.DECIDUOUS])
        self.hugs += total_deciduous + 1
        print('You have hugged ' + str(self.hugs) + ' trees <3')
        sleep(0.5)


if __name__ == '__main__':
    player = Player(1, 'Seb')
    player.assign_bonus_card()
    player.draw_tree_card()

    print('Player: {}'.format(player.name))

    can_plant_tree = player.can_plant_tree(player.hand[0])
    print('Can plant {}? {}'.format(player.hand[0].common_name, can_plant_tree))
