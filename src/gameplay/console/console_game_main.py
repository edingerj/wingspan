from abc import ABC
from typing import Optional

from gameplay.base import GameMain
from gameplay.base.io import Info, Move, TurnPhase
from gameplay.console.io.console_input import *
from gameplay.console.io.console_output import *
from player import Player, Players
from tree import Nutrients, TreeCard


class ConsoleGameMain(GameMain, ABC):
    def __init__(self: 'ConsoleGameMain', players: Players, total_turns: int) -> None:
        super(ConsoleGameMain, self).__init__(players, total_turns)

    def output_start_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_start_turn(player, self.turns_remaining)

    def output_end_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print_end_turn(player)

    def input_information(self: 'ConsoleGameMain', player: Player, turn_phase: TurnPhase) -> Info:
        return get_information(player, turn_phase)

    def output_information(self: 'ConsoleGameMain', player: Player, info: Info) -> None:
        print_information(player, self.displayed_tree_cards, info)

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

    def output_draw_tree_cards(self: 'ConsoleGameMain', player: Player, number: int) -> None:
        print_draw_tree_cards(number)

    def input_draw_tree_card_index(self: 'ConsoleGameMain', player: Player) -> int:
        return input_draw_tree_card_index(self.displayed_tree_cards)

    def output_draw_tree_card(self: 'ConsoleGameMain', player: Player, tree_card: TreeCard, was_random=False) -> None:
        print_draw_tree_card(tree_card, was_random=was_random)

    def output_end_game(self: 'ConsoleGameMain') -> None:
        print_results(self.players)
