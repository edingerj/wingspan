from abc import ABCMeta, abstractmethod
from typing import Final, List

from game.game_results import GameResults
from game.move import Move
from player import Hand, Player
from tree import Nutrients, TreeCard


class GameMain(metaclass=ABCMeta):
    def __init__(self: 'GameMain', all_players: List[Player], total_turns: int) -> None:
        self.all_players: Final[List[Player]] = all_players
        self.displayed_tree_cards: Final[Hand] = Hand.from_deck()
        self.total_turns: Final[int] = total_turns
        self.turns_remaining: int = total_turns * len(all_players)

    def start_game(self: 'GameMain') -> None:
        self.take_turn(self.all_players[0])

    @abstractmethod
    def take_turn(self: 'GameMain', player: Player) -> None:
        pass

    @abstractmethod
    def start_turn(self: 'GameMain', player: Player) -> None:
        pass

    @abstractmethod
    def end_turn(self: 'GameMain', player: Player) -> None:
        self.turns_remaining -= 1
        if self.turns_remaining > 0:
            self.take_turn(self.get_next_player(player))
        else:
            self.end_game()

    @abstractmethod
    def retry_turn(self: 'GameMain', player: Player) -> None:
        self.take_turn(player)

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
    def plant_tree(self: 'GameMain', player: Player) -> None:
        pass

    @abstractmethod
    # hug 1 additional tree for each Deciduous tree in arb
    def hug_trees(self: 'GameMain', player: Player) -> int:
        return player.hug_trees()

    @abstractmethod
    # gain 1 additional nutrient card for every Conifer tree in arb
    def draw_nutrient_cards(self: 'GameMain', player: Player) -> Nutrients:
        return player.draw_nutrient_cards()

    @abstractmethod
    # draw 1 additional tree card for each Urban tree in arb
    def draw_tree_cards(self: 'GameMain', player: Player) -> None:
        pass

    @abstractmethod
    def draw_chosen_tree_card(self: 'GameMain', player: Player, choice_index: int) -> TreeCard:
        tree_card = self.displayed_tree_cards.pop(choice_index)     # remove card from display
        player.hand.append(tree_card)                               # add it to player's hand
        self.displayed_tree_cards.draw_from_deck()                  # refresh display
        return tree_card

    @abstractmethod
    def draw_random_tree_card(self: 'GameMain', player: Player) -> TreeCard:
        return player.draw_tree_card()

    def get_next_player(self: 'GameMain', current_player: Player) -> Player:
        player_index = self.all_players.index(current_player)
        if player_index == len(self.all_players) - 1:
            return self.all_players[0]
        else:
            return self.all_players[player_index + 1]

    @abstractmethod
    def end_game(self: 'GameMain') -> None:
        pass

    def get_results(self: 'GameMain') -> GameResults:
        return GameResults(self.all_players)
