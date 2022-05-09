from typing import List

from console.sleep import sleep
from game import GameResults
from player import Player
from tree import Nutrients, TreeCard


def print_welcome_message() -> None:
    print(
        '┌{}┐\n'.format(73 * '─') +
        '│{}│\n'.format('Welcome to Treespan'.center(73)) +
        '└{}┘\n'.format(73 * '─')
    )


def print_start_turn(player: Player, turns_remaining: int) -> None:
    sleep(1)
    print('\n{} {}'.format(
        'It\'s {}\'s turn!'.format(player.name).ljust(54),
        'Turns Remaining: {}'.format(turns_remaining).rjust(20),
    ))
    print(player)


def print_end_turn(player: Player) -> None:
    print(player)
    input(
        'Enter any key to end your turn:\n' +
        '  → ')
    return


def print_retry_move() -> None:
    print('Let\'s try this again', end='')
    print_ellipsis()


def print_plant_tree(player: Player, tree_card: TreeCard) -> None:
    print('Checking if you have enough nutrients to plant a {}'.format(tree_card.common_name), end='')
    print_ellipsis()
    if player.can_plant_tree(tree_card):
        print('*** planting a {} ***'.format(tree_card.common_name))
        sleep(1)
        print('  Your combined tree height is: {}'.format(player.arboretum.get_total_height() + tree_card.height))
        sleep(0.5)
    else:
        print('Sorry, you don\'t have enough nutrients to plant a {}.'.format(tree_card.common_name))


def print_hug_trees(player: Player, trees_hugged: int) -> None:
    sleep(0.5)
    print('*** hugging tree{} ***'.format('s' if (trees_hugged != 1) else ''))
    sleep(0.5)
    print('  You have hugged {} tree{} <3'.format(player.hugs, 's' if (player.hugs != 1) else ''))


def print_draw_nutrient_cards(player: Player, nutrients: Nutrients) -> None:
    sleep(0.5)
    print('*** rolling di{}e ***'.format('c' if (len(nutrients) != 1) else ''))
    for nutrient in nutrients:
        sleep(0.25)
        print('  You rolled a {}! Adding it to your pile of nutrients.'.format(nutrient.emoji()))


def print_draw_tree_card(tree_card: TreeCard, was_random=False) -> None:
    if was_random:
        print('Drawing a random card from the deck', end='')
        print_ellipsis(delay=0.25)
    print('You drew a {}!'.format(tree_card.common_name))


def print_results(all_players: List[Player], results: GameResults) -> None:
    print('\n*** GAME OVER ***\nAdding up points', end='')
    print_ellipsis()
    print_line()

    print('Step 1: Add up all tree points.')
    for player in all_players:
        print('  {} has earned {} tree points.'.format(player.name, player.get_total_tree_points()))
    input_line()

    print('Step 2: Count the number of trees hugged.')
    for player in all_players:
        print('  {} has hugged {} trees.'.format(player.name, player.hugs))
    input_line()

    print('Step 3: Add up bonus points.')
    for player in all_players:
        print('  {}, a {}, has earned {} bonus points.'
              .format(player.name, player.bonus_class.name, player.get_total_bonus_points()))
    input_line()

    print('Final Step: Take the sum of all points.')
    print_line()

    # Todo: its a tie!
    print('And the winner is', end='')
    print_ellipsis(end=' ')
    print('{}! Congratulations!'.format(results.winning_player.name))

    # Todo: pretty print ranked results table
    #  with duplicate ranks as appropriate
    print('\nTotal Points:')
    for index, player in enumerate(all_players):
        print('  {}: {} pts'.format(player.name, results.player_scores[index]))


def print_line() -> None:
    print(75 * '─')
    sleep(0.5)


def input_line() -> None:
    input(75 * '─')
    sleep(0.5)


def print_ellipsis(delay: float = 0.5, end: str = '\n') -> None:
    for _ in range(3):
        print('.', end='')
        sleep(delay)
    if end != '':
        print('', end=end)


__all__ = [
    'print_welcome_message',
    'print_start_turn',
    'print_end_turn',
    'print_retry_move',
    'print_plant_tree',
    'print_hug_trees',
    'print_draw_nutrient_cards',
    'print_draw_tree_card',
    'print_results',
    'print_ellipsis',
]
