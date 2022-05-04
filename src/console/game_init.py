from game import game_instance
from console.sleep import sleep
from player import all_players, Player


def initialize_game() -> None:
    game_instance.set_num_players(get_num_players())
    game_instance.set_total_turns(get_total_turns())
    add_players()


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


def add_players() -> None:
    for index in range(game_instance.num_players):
        add_player(index)

    for player in all_players:
        player.assign_bonus_card()
        player.draw_nutrient_cards(3)

    sleep(0.5)
    print('\nSetting up the game board...')

    for player in all_players:
        sleep(0.5)
        print(player.to_string())


def add_player(index: int) -> None:
    name = input(
        'Player {}, enter your name:\n'.format(index + 1) +
        '  → ')
    player = Player(index + 1, name)
    all_players.append(player)
