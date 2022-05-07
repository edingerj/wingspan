from typing import List

from bonus.bonus_classes import BonusClasses
from console.console_game_main import ConsoleGameMain
from console.console_output import print_ellipsis
from console.sleep import sleep
from game import game_instance
from player import Player, PlayerName


# Todo: add console colors, potentially?
#  See: https://gist.github.com/dnmellen/5584007

def main() -> None:
    game_instance.set(initialize_game())
    print_game_setup(game_instance.get().all_players)
    game_instance.get().start_game()


def initialize_game() -> ConsoleGameMain:
    print('Welcome to Wingspan (tree edition)!', end='\n\n')
    num_players = get_num_players()
    total_turns = get_total_turns()
    all_players = get_players(num_players)
    return ConsoleGameMain(all_players, total_turns)


def get_num_players() -> int:
    num_players = input_num_players()
    while num_players not in ('2', '3', '4'):
        print('{} is not a valid number of players.'.format(num_players))
        num_players = input_num_players()
    return int(num_players)


def input_num_players() -> str:
    return input(
        'How many players are there? (2, 3, or 4):\n' +
        '  → ')


def get_total_turns() -> int:
    total_turns = input_total_turns()
    while total_turns not in [str(num) for num in range(1, 100)]:
        print('{} is not a valid number of turns.'.format(total_turns))
        total_turns = input_total_turns()
    print()
    return int(total_turns)


def input_total_turns() -> str:
    return input(
        'How many turns would you like to play? (1 to 99):\n' +
        '  → ')


# player is given a bonus class randomly
# Todo: implement choice of bonus class
def get_players(num_players: int) -> List[Player]:
    player_names = [get_player_name(index) for index in range(num_players)]
    bonus_classes = BonusClasses.established()

    return [Player(player_names[index], bonus_classes[index]) for index in range(num_players)]


def get_player_name(index: int) -> PlayerName:
    print('Player {}, enter your name:'.format(index + 1))
    player_name = input_player_name()
    while not player_name.valid():
        if not player_name.min_length_validator():
            print('Please enter a name:')
        if not player_name.max_length_validator():
            print('The name: {}... is too long.\nPlease enter a shorter name:'
                  .format(player_name[PlayerName.max_length - 3:]))
        if not player_name.unique_validator():
            print('The name: {} has already been taken.\nPlease enter a different name:'
                  .format(player_name))
        player_name = input_player_name()
    player_name.save()
    return player_name


def input_player_name() -> PlayerName:
    return PlayerName.of(input('  → '))


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
