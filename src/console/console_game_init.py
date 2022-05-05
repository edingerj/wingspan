from typing import List

from console.console_game_main import ConsoleGameMain
from console.console_print import print_ellipsis
from console.sleep import sleep
from game import game_instance
from player import Player


def main() -> None:
    print('Welcome to Wingspan (tree edition)!', end='\n\n')
    game_instance.set(initialize_game())
    print_game_setup(game_instance.get().all_players)
    game_instance.get().start_game()


def initialize_game() -> ConsoleGameMain:
    num_players = get_num_players()
    total_turns = get_total_turns()
    all_players = get_players(num_players)
    return ConsoleGameMain(all_players, total_turns)


def get_num_players() -> int:
    num_players: int = input_num_players()
    while num_players not in range(2, 5):
        print('{} is not a valid number of players'.format(num_players))
        num_players = input_num_players()
    return num_players


def input_num_players() -> int:
    return int(input(
        'Enter the number of players (2, 3, or 4):\n' +
        '  → '))


def get_total_turns() -> int:
    total_turns: int = input_total_turns()
    while total_turns not in range(1, 100):
        print('{} is not a valid number of turns'.format(total_turns))
        total_turns = input_total_turns()
    return total_turns


def input_total_turns() -> int:
    return int(input(
        'How many turns would you like to play?\n' +
        '  → '))


def get_players(num_players: int) -> List[Player]:
    all_players = [get_player(index) for index in range(num_players)]

    for player in all_players:
        player.assign_bonus_card()

    return all_players


def get_player(index: int) -> Player:
    name = input_player_name(index)
    while len(name) not in range(1, 50):
        print('{} is not a valid player name'.format(name))
        name = input_player_name(index)
    return Player(name)


def input_player_name(index: int) -> str:
    return input(
        'Player {}, enter your name:\n'.format(index + 1) +
        '  → ')


def print_game_setup(all_players: List[Player]) -> None:
    sleep(0.5)
    print('\nSetting up the game board', end='')
    print_ellipsis(end='\n\n')

    for player in all_players:
        sleep(0.5)
        print(player.to_string())

    input(
        'Are you ready to start?\n'
        'Enter any key to begin:\n' +
        '  → ')
