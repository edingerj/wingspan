from abc import ABC
from typing import List, Optional

from console.console_input import get_move, input_retry_plant_tree, select_draw_tree_card, select_plant_tree_card
from console.console_print import print_results, print_hug_trees, print_draw_nutrient_cards, print_draw_tree_card, \
    print_retry_turn, print_start_turn, print_end_turn, print_plant_tree
from game import GameMain
from player import Player
from tree import Habitat, TreeCard


class ConsoleGameMain(GameMain, ABC):
    def __init__(self: 'ConsoleGameMain', all_players: List[Player], total_turns: int) -> None:
        super(ConsoleGameMain, self).__init__(all_players, total_turns)

    def take_turn(self: 'ConsoleGameMain', player: Player) -> None:
        self.start_turn(player)
        move = get_move(player)
        self.do_move(player, move)
        self.end_turn(player)

    def start_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_start_turn(player, self.all_players, self.turns_remaining)

    def end_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_end_turn(player)
        super(ConsoleGameMain, self).end_turn(player)

    def retry_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_retry_turn()
        super(ConsoleGameMain, self).retry_turn(player)

    def plant_tree(self: 'ConsoleGameMain', player: Player) -> None:
        choice_index = select_plant_tree_card(player.hand)
        tree_card: Optional[TreeCard] = player.hand[choice_index] if (choice_index is not None) else None
        if tree_card is not None:
            print_plant_tree(player, tree_card)
            if player.can_plant_tree(tree_card):
                return player.plant_tree(tree_card)
        self.retry_plant_tree(player)

    def retry_plant_tree(self: 'ConsoleGameMain', player: Player) -> None:
        choice = input_retry_plant_tree()
        if choice == 1:
            self.plant_tree(player)
        elif choice == 2:
            self.retry_turn(player)

    # hug 1 additional tree for each Deciduous tree in arb
    def hug_trees(self: 'ConsoleGameMain', player: Player) -> None:
        trees_hugged = super(ConsoleGameMain, self).hug_trees(player)
        print_hug_trees(player, trees_hugged)

    # gain 1 additional nutrient card for every Conifer tree in arb
    def draw_nutrient_cards(self: 'ConsoleGameMain', player: Player) -> None:
        nutrients = super(ConsoleGameMain, self).draw_nutrient_cards(player)
        print_draw_nutrient_cards(player, nutrients)

    # draw 1 additional tree card for each Urban tree in arb
    def draw_tree_cards(self: 'ConsoleGameMain', player: Player) -> None:
        total_urban = len(player.arboretum[Habitat.URBAN])
        for _ in range(total_urban + 1):
            choice_index = select_draw_tree_card(self.displayed_tree_cards)
            if choice_index in range(len(self.displayed_tree_cards)):
                self.draw_chosen_tree_card(player, choice_index)
            elif choice_index == len(self.displayed_tree_cards):
                self.draw_random_tree_card(player)

    def draw_chosen_tree_card(self: 'ConsoleGameMain', player: Player, choice: int) -> None:
        tree_card = super(ConsoleGameMain, self).draw_chosen_tree_card(player, choice)
        print_draw_tree_card(tree_card)

    def draw_random_tree_card(self: 'ConsoleGameMain', player: Player) -> None:
        tree_card = super(ConsoleGameMain, self).draw_random_tree_card(player)
        print_draw_tree_card(tree_card, was_random=True)

    def end_game(self: 'ConsoleGameMain') -> None:
        print_results(self.all_players, self.get_results())
