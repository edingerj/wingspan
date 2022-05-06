from typing import List

from console.sleep import sleep
from game import GameResults
from player import Player
from tree import Nutrients, TreeCard


def print_start_turn(player: Player, all_players: List[Player], turns_remaining: int) -> None:
    sleep(0.5)
    # Todo: switch Turns Remaining to only decrement after last players turn (in round)
    print('\nTurns remaining: ' + str(round(turns_remaining / len(all_players))))
    sleep(0.5)
    print('\nIt\'s {}\'s turn!'.format(player.name))
    sleep(0.5)
    print(player.to_string())


def print_end_turn(player: Player) -> None:
    print(player.to_string())
    input(
        'Enter any key to end your turn:\n' +
        '  → ')
    return


def print_retry_turn() -> None:
    print('Let\'s try this again', end='')
    print_ellipsis(end='\n')


def print_plant_tree(player: Player, tree_card: TreeCard) -> None:
    print('Checking if you have enough nutrients to plant a {}...'.format(tree_card.common_name))
    sleep(0.5)
    if player.can_plant_tree(tree_card):
        print('*** planting a {} ***'.format(tree_card.common_name))
        sleep(0.5)
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
    sleep(0.25)
    print('*** rolling di{}e ***'.format('c' if (len(nutrients) != 1) else ''))
    for nutrient in nutrients:
        sleep(0.25)
        print('  You rolled a {}! Adding it to your pile of nutrients.'.format(nutrient.to_emoji()))


def print_draw_tree_card(tree_card: TreeCard, was_random: bool = False) -> None:
    if was_random:
        print('Drawing a random card from the deck', end='')
        print_ellipsis(delay=0.25, end='\n')
    print('You drew a {}!'.format(tree_card.common_name))


def print_results(all_players: List[Player], results: GameResults) -> None:
    print('\n*** GAME OVER ***\nAdding up points', end='')
    print_ellipsis(end='\n')
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

    print('And the winner is', end='')
    print_ellipsis(end=' ')
    print('{}! Congratulations!'.format(results.winning_player.name))

    print('\nTotal Points:')
    for index, player in enumerate(all_players):
        print('  {}: {} pts'.format(player.name, results.player_scores[index]))


def print_line() -> None:
    print(75 * '-')
    sleep(0.5)


def input_line() -> None:
    input(75 * '-')
    sleep(0.5)


def print_ellipsis(delay: float = 0.5, end: str = '') -> None:
    for _ in range(3):
        print('.', end='')
        sleep(delay)
    if end != '':
        print('', end=end)
