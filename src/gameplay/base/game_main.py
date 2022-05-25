from abc import ABCMeta, abstractmethod
from typing import Final, Optional

from gameplay.base.bonus_applictor import BonusApplicator
from gameplay.base.io import Info, Move, TurnPhase
from player import Hand, Player, Players
from tree import Habitat, Nutrients, TreeCard


class GameMain(metaclass=ABCMeta):
    def __init__(self: 'GameMain', players: Players, total_turns: int) -> None:
        self.players: Final[Players] = players
        self.displayed_tree_cards: Final[Hand] = Hand.from_deck()
        self.total_turns: Final[int] = total_turns
        self.turns_remaining: int = total_turns

    def start_game(self: 'GameMain') -> None:
        self.take_turn(self.players[0])

    def take_turn(self: 'GameMain', player: Player) -> None:
        self.start_turn(player)
        self.start_move(player)
        self.end_turn(player)

    def start_turn(self: 'GameMain', player: Player) -> None:
        self.output_start_turn(player)
        self.start_information(player, TurnPhase.STARTING)

    @abstractmethod
    def output_start_turn(self: 'GameMain', player: Player) -> None:
        pass

    def end_turn(self: 'GameMain', player: Player) -> None:
        BonusApplicator(self.players).apply_bonuses()
        if player == self.players[-1]:
            self.turns_remaining -= 1
        self.start_information(player, TurnPhase.ENDING)
        if self.turns_remaining > 0:
            self.take_turn(self.players.next(player))
        else:
            self.end_game()

    @abstractmethod
    def output_end_turn(self: 'GameMain', player: Player) -> None:
        pass

    def start_information(self: 'GameMain', player: Player, turn_phase: TurnPhase) -> None:
        info = self.input_information(player, turn_phase)
        while info is not Info.CONTINUE:
            self.output_information(player, info)
            info = self.input_information(player, turn_phase)

    @abstractmethod
    def input_information(self: 'GameMain', player: Player, turn_phase: TurnPhase) -> Info:
        pass

    @abstractmethod
    def output_information(self: 'GameMain', player: Player, info: Info) -> None:
        pass

    def start_move(self: 'GameMain', player: Player) -> None:
        move = self.input_move(player)
        self.do_move(player, move)

    def do_move(self: 'GameMain', player: Player, move: Move) -> None:
        if move == Move.PLANT_TREE:
            self.plant_tree(player)
        elif move == Move.HUG_TREES:
            self.hug_trees(player)
        elif move == Move.DRAW_NUTRIENTS:
            self.draw_nutrient_cards(player)
        elif move == Move.DRAW_TREES:
            self.draw_tree_cards(player)

    @abstractmethod
    def input_move(self: 'GameMain', player: Player) -> Move:
        pass

    def retry_move(self: 'GameMain', player: Player, current_move: Move) -> None:
        choice = self.input_retry_move(player)
        if choice == 1:
            self.do_move(player, current_move)
        elif choice == 2:
            self.output_retry_move(player)
            self.start_move(player)

    @abstractmethod
    def input_retry_move(self: 'GameMain', player: Player) -> int:
        pass

    @abstractmethod
    def output_retry_move(self: 'GameMain', player: Player) -> None:
        pass

    def plant_tree(self: 'GameMain', player: Player) -> None:
        tree_card = self.input_plant_tree_card(player)
        if tree_card is not None:
            self.output_plant_tree_card(player, tree_card)
            if player.can_plant_tree(tree_card):
                return player.plant_tree(tree_card)
        self.retry_move(player, Move.PLANT_TREE)

    @abstractmethod
    def input_plant_tree_card(self: 'GameMain', player: Player) -> Optional[TreeCard]:
        pass

    @abstractmethod
    def output_plant_tree_card(self: 'GameMain', player: Player, tree_card: TreeCard) -> None:
        pass

    # hug 1 additional tree for each Deciduous tree in arb
    def hug_trees(self: 'GameMain', player: Player) -> None:
        trees_hugged = player.hug_trees()
        self.output_hug_trees(player, trees_hugged)

    @abstractmethod
    def output_hug_trees(self: 'GameMain', player: Player, trees_hugged: int) -> None:
        pass

    # gain 1 additional nutrient card for every Coniferous tree in arb
    def draw_nutrient_cards(self: 'GameMain', player: Player) -> None:
        nutrients = player.draw_nutrient_cards()
        self.output_draw_nutrient_cards(player, nutrients)

    @abstractmethod
    def output_draw_nutrient_cards(self: 'GameMain', player: Player, nutrients: Nutrients) -> None:
        pass

    # draw 1 additional tree card for each Urban tree in arb
    # Todo: handle cases of empty deck & no cards to draw
    def draw_tree_cards(self: 'GameMain', player: Player) -> None:
        total_urban = len(player.arboretum[Habitat.URBAN])
        self.output_draw_tree_cards(player, total_urban + 1)
        for _ in range(total_urban + 1):
            choice_index = self.input_draw_tree_card_index(player)
            if choice_index in range(len(self.displayed_tree_cards)):
                self.draw_displayed_tree_card(player, choice_index)
            elif choice_index == len(self.displayed_tree_cards):
                self.draw_random_tree_card(player)

    @abstractmethod
    def output_draw_tree_cards(self: 'GameMain', player: Player, number: int) -> None:
        pass

    @abstractmethod
    def input_draw_tree_card_index(self: 'GameMain', player: Player) -> int:
        pass

    def draw_displayed_tree_card(self: 'GameMain', player: Player, choice_index: int) -> None:
        tree_card = self.displayed_tree_cards.pop(choice_index)     # remove card from display
        player.draw_tree_card_from_display(tree_card)               # add it to player's hand
        self.displayed_tree_cards.draw_from_deck()                  # refresh display
        self.output_draw_tree_card(player, tree_card)

    def draw_random_tree_card(self: 'GameMain', player: Player) -> None:
        tree_card = player.draw_tree_card_from_deck()
        self.output_draw_tree_card(player, tree_card, was_random=True)

    @abstractmethod
    def output_draw_tree_card(self: 'GameMain', player: Player, tree_card: TreeCard, was_random=False) -> None:
        pass

    def end_game(self: 'GameMain') -> None:
        self.output_end_game()

    @abstractmethod
    def output_end_game(self: 'GameMain') -> None:
        pass
