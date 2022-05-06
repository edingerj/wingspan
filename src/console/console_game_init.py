from typing import List

from bonus.bonus_classes import BonusClasses
from console.console_game_main import ConsoleGameMain
from console.console_output import print_ellipsis
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


# Todo: sanitise input
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


# Todo: sanitise input
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


# player is given a bonus class randomly
# Todo: implement choice of bonus class
def get_players(num_players: int) -> List[Player]:
    player_names = [get_player_name(index) for index in range(num_players)]
    bonus_classes = BonusClasses.established()

    return [Player(player_names[index], bonus_classes[index]) for index in range(num_players)]


# Todo: require unique player names
def get_player_name(index: int) -> str:
    name = input_player_name(index)
    while len(name) not in range(1, 50):
        print('{} is not a valid player name'.format(name))
        name = input_player_name(index)
    return name


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
        print(player)

    input(
        'Are you ready to start?\n'
        'Enter any key to begin:\n' +
        '  → ')
