from typing import List

from bonus import BonusCard, BonusCards
from console.console_game_main import ConsoleGameMain
from console.console_output import print_welcome_message, print_ellipsis
from console.console_runtime_flags import ConsoleRuntimeFlags
from console.sleep import sleep
from game import game_instance, runtime_flags
from player import Player, PlayerName, Players


# Todo: add console colors, potentially?
#  See: https://gist.github.com/dnmellen/5584007

def main(arguments: List[str]) -> None:
    runtime_flags.set(ConsoleRuntimeFlags.from_arguments(arguments))
    game_instance.set(initialize_game())
    print_game_setup(game_instance.get().players)
    game_instance.get().start_game()


def initialize_game() -> ConsoleGameMain:
    print_welcome_message()
    num_players = get_num_players()
    total_turns = get_total_turns()
    bonus_cards = get_bonus_cards()
    players = get_players(num_players, bonus_cards)
    return ConsoleGameMain(players, total_turns)


def get_num_players() -> int:
    num_players = input_num_players()
    while num_players not in ('2', '3', '4'):
        print('{} is not a valid number of players.'.format(num_players))
        num_players = input_num_players()
    return int(num_players)


def input_num_players() -> str:
    return input(
        'How many players do you have? (2, 3, or 4):\n' +
        '  → ').strip()


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
        '  → ').strip()


def get_bonus_cards() -> BonusCards:
    return BonusCards.all() if runtime_flags.get().experimental else BonusCards.established()


def get_players(num_players: int, bonus_cards: BonusCards) -> Players:
    player_names = [get_player_name(index) for index in range(num_players)]
    print()
    player_bonus_cards = [get_player_bonus_card(bonus_cards, player_names[index]) for index in range(num_players)]
    print()

    return Players(
        [Player(player_names[index], player_bonus_cards[index]) for index in range(num_players)]
    )


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
    return PlayerName.of(input('  → ').strip())


def get_player_bonus_card(bonus_cards: BonusCards, player_name: PlayerName) -> BonusCard:
    choice = input_player_bonus_card(bonus_cards, player_name)
    bonus_card_index = bonus_cards.index_of(choice)
    while bonus_card_index is None:
        choice = retry_input_player_bonus_card(choice)
        bonus_card_index = bonus_cards.index_of(choice)
    return bonus_cards.pop(bonus_card_index)


def input_player_bonus_card(bonus_cards: BonusCards, player_name: PlayerName) -> str:
    return input(
        '{}, you may draw one of the following bonus cards:\n'.format(player_name) +
        '{}\n'.format(bonus_cards) +
        '  → ').strip()


def retry_input_player_bonus_card(previous_choice: str) -> str:
    return input(
        'Invalid bonus selection: {}. Please try again:\n'.format(previous_choice) +
        '  → ').strip()


def print_game_setup(players: Players) -> None:
    sleep(0.5)
    print('Setting up the game board', end='')
    print_ellipsis(end='\n\n')

    for player in players:
        sleep(0.5)
        print(player)

    input(
        'Are you ready to start?\n'
        'Enter any key to begin:\n' +
        '  → ')
