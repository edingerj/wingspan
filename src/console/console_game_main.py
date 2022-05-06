from abc import ABC
from typing import List, Optional

from console.console_input import *
from console.console_output import *
from game import GameMain, GameResults, Move
from player import Player
from tree import Nutrients, TreeCard


class ConsoleGameMain(GameMain, ABC):
    def __init__(self: 'ConsoleGameMain', all_players: List[Player], total_turns: int) -> None:
        super(ConsoleGameMain, self).__init__(all_players, total_turns)

    def output_start_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_start_turn(player, self.turns_remaining)

    def output_end_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_end_turn(player)

    def input_move(self: 'ConsoleGameMain', player: Player) -> Move:
        return get_move(player)

    def input_retry_move(self: 'ConsoleGameMain', player: Player) -> int:
        return input_retry_plant_tree()

    def output_retry_move(self: 'ConsoleGameMain', player: Player) -> None:
        print_retry_move()

    def input_plant_tree_card(self: 'ConsoleGameMain', player: Player) -> Optional[TreeCard]:
        choice_index = select_plant_tree_card(player.hand)
        return player.hand[choice_index] if (choice_index is not None) else None

    def output_plant_tree_card(self: 'ConsoleGameMain', player: Player, tree_card: TreeCard) -> None:
        print_plant_tree(player, tree_card)

    def output_hug_trees(self: 'ConsoleGameMain', player: Player, trees_hugged: int) -> None:
        print_hug_trees(player, trees_hugged)

    def output_draw_nutrient_cards(self: 'ConsoleGameMain', player: Player, nutrients: Nutrients) -> None:
        print_draw_nutrient_cards(player, nutrients)

    def input_draw_tree_card_index(self: 'ConsoleGameMain', player: Player) -> int:
        return input_draw_tree_card_index(self.displayed_tree_cards)

    def output_draw_tree_card(self: 'ConsoleGameMain', player: Player, tree_card: TreeCard, was_random=False) -> None:
        print_draw_tree_card(tree_card, was_random=was_random)

    def output_end_game(self: 'ConsoleGameMain', game_results: GameResults) -> None:
        print_results(self.all_players, game_results)
