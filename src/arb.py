"""
Players have 4 options every turn:
1) Plant a tree
2) Hug a tree
3) Gain nutrients: sun, water, fire, disturbance
4) Draw tree cards
"""

from typing import List

from console import sleep, initialize_game
from game import game_instance, Move
from player import Player, all_players, computer
from tree import Habitat, TreeCard

# Globals
height_list: List[int]


def main() -> None:
    print('Welcome to Wingspan (tree edition)!')
    initialize_game()
    input('Are you ready to start? Enter any key to begin. ')
    take_a_turn(all_players[0])


def retry_plant_tree(player: Player) -> None:
    option = input(
        '  1. Select another tree card\n'
        '  2. Go back to the main menu\n' +
        '  → ')
    while option != '1' and option != '2':
        option = input('Invalid input. Enter (1) or (2): ')
    if option == '1':
        plant_tree(player)
    if option == '2':
        retry_turn(player)


def plant_tree(player: Player) -> None:
    choice = input(
        'Select a tree card to play:\n' +
        '  → ')
    tree_card: TreeCard = next(filter(lambda card: card.common_name.lower() == choice.lower(), player.hand), None)
    if tree_card is not None:
        print('Checking if you have enough nutrients to plant a {}...'.format(tree_card.common_name))
        sleep(0.5)
        if player.can_plant_tree(tree_card):
            player.plant_tree(tree_card)
            print('Planting a {}...'.format(tree_card.common_name))
            sleep(0.5)
            print('Your combined tree height is: {}'.format(player.combined_height))
            sleep(0.5)
        else:
            print('Sorry, you don\'t have enough nutrients to plant a {}.'.format(tree_card.common_name))
            retry_plant_tree(player)
    else:
        print('You don\'t have a {} in your hand.'.format(choice))
        retry_plant_tree(player)


# hug 1 additional tree for each Deciduous tree in arb
def hug_trees(player: Player) -> None:
    sleep(0.2)
    hugs = player.hug_trees()
    print('*** hugging {} tree{} ***'.format(hugs, 's' if (hugs != 1) else ''))
    sleep(0.2)
    print('  {} has hugged {} trees <3'.format(player.name, player.hugs))


# gain 1 additional nutrient card for every Conifer in arb
def draw_nutrient_cards(player: Player) -> None:
    sleep(0.2)
    print('*** rolling dice ***')
    nutrients = player.draw_nutrient_cards()
    for nutrient in nutrients:
        sleep(0.2)
        print('  {0} rolled a {1}! Adding it to {0}\'s pile of nutrients...'.format(player.name, nutrient.to_emoji()))


# draw 1 additional tree card for each Urban tree in arb
def draw_tree_cards(player: Player) -> None:
    total_urban = len(player.arboretum[Habitat.URBAN])
    for i in range(total_urban + 1):
        choice = int(input(
            'Select from the following cards:\n' +
            '{}\n'.format(computer.hand.to_string()) +
            '  4. random card from the deck\n'
            '  → '))
        while choice not in range(1, 5):
            choice = int(input(
                'Invalid input. Enter 1, 2, 3, or 4 for a random card:\n' +
                '  → '))
        if choice in range(1, 4):
            draw_chosen_card(player, choice)
        elif choice == 4:
            draw_random_card(player)


def draw_chosen_card(player: Player, choice: int) -> None:
    chosen_card = computer.hand.pop(int(choice) - 1)  # remove it from display
    player.hand.append(chosen_card)  # add it to player's hand
    computer.draw_tree_card()  # refresh display
    print('You drew a {}!'.format(chosen_card.common_name))


def draw_random_card(player: Player) -> None:
    print('Drawing random card from deck...')
    tree_card = player.draw_tree_card()
    print('You drew a {}!'.format(tree_card))


def next_player(current_player: Player) -> Player:
    player_index = all_players.index(current_player)
    if player_index == len(all_players) - 1:
        return all_players[0]
    else:
        return all_players[player_index + 1]


def evaluate_bonus_cards(player: Player):
    all_trees = player.arboretum.get_all_trees()
    if player.bonus.name == 'michigander':
        for tree in all_trees:
            if tree.michigander == 1:
                player.bonus_points += 2
    # if player.bonus.name == 'tree climber': # get 10 point bonus if you have the tallest combined height
    # anyone can get 10 bonus points for having highest combined height, like longest roads in Catan
    global height_list
    if 0 < max(height_list) == player.combined_height:
        player.bonus_points += 10
    return player.bonus_points


def get_total_score(player: Player):
    # return a list [tree points, hugs, bonus points]
    # tree_points = 0

    # Add tree points
    all_trees = player.arboretum.get_all_trees()
    for tree in all_trees:
        player.tree_points += tree.points
    # player.combined_height += tree.height
    # Add bonus points

    # print('The combined height of your trees is ' + str(player.combined_height))

    player.bonus_points = evaluate_bonus_cards(player)

    return [player.tree_points, player.hugs, player.bonus_points]


def end_game():
    global height_list
    print('\n*** GAME OVER ***\nAdding up points...')
    sleep(0.5)

    height_list = [player.combined_height for player in all_players]
    player_scores = [get_total_score(player) for player in all_players]
    player_score_totals = [sum(scores) for scores in player_scores]
    winning_player = all_players[player_score_totals.index(max(player_score_totals))]

    print(75 * "-")
    sleep(0.5)

    print('Step 1: Add up all tree points.')
    for player in all_players:
        print('  {} has earned {} tree points.'.format(player.name, player.tree_points))
    input(75 * "-")
    sleep(0.5)

    print('Step 2: Count the number of trees hugged.')
    for player in all_players:
        print('  {} has hugged {} trees.'.format(player.name, player.hugs))
    input(75 * "-")
    sleep(0.5)

    print('Step 3: Add up bonus points.')
    for player in all_players:
        print('  {}, a {}, has earned {} bonus points.'.format(player.name, player.bonus.name, player.bonus_points))
    input(75 * "-")
    sleep(0.5)

    print('Final Step: Take the sum of all points.')
    print(75 * "-")
    sleep(0.5)

    input('And the winner is...')
    print('\n{}! Congratulations!'.format(winning_player.name))

    print('\nTotal Points:')
    for index, player in enumerate(all_players):
        print('  {}: {} pts'.format(player.name, player_score_totals[index]))


def retry_turn(player: Player) -> None:
    game_instance.turns_remaining += 1
    print("Let's try this again...\n")
    sleep(0.5)
    take_a_turn(player)


def take_a_turn(player: Player):
    sleep(0.5)
    print('Turns remaining: ' + str(round(game_instance.turns_remaining / len(all_players))))
    game_instance.turns_remaining -= 1
    print('\nIt\'s {}\'s turn!'.format(player.name))
    print(player.to_string())
    print('{}, '.format(player.name), end='')

    move = Move.from_console()
    if move == Move.PLANT_TREE:  # Plant a tree
        plant_tree(player)
    elif move == Move.HUG_TREES:  # Hug a tree
        hug_trees(player)
    elif move == Move.DRAW_NUTRIENTS:  # Gain nutrients
        draw_nutrient_cards(player)
    elif move == Move.DRAW_TREES:  # Draw tree cards
        draw_tree_cards(player)

    print(player.to_string())
    input('Enter "z" to end your turn. ')
    if game_instance.turns_remaining > 0:
        take_a_turn(next_player(player))
    else:
        end_game()


if __name__ == '__main__':
    # welcome_message()
    main()
