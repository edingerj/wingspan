"""
Players have 4 options every turn:
1) Plant a tree
2) Gain nutrients: sun, water, fire, disturbance
3) Hug a tree
4) Draw tree cards
"""

import time
from typing import List, Optional

from gameplay import Move
from player import Player
from tree import Nutrient, Habitat

# Globals
computer: Player = Player()
turns_remaining: int

num_players: int
all_players: List[Player]
player_1: Player
player_2: Player
player_3: Optional[Player]
player_4: Optional[Player]

height_list: List[int] = []


def draw_chosen_card(hand, choice):
    i = int(choice) - 1
    chosen_card = computer.hand.pop(i)  # remove it from display
    hand.append(chosen_card)  # add it to player's hand
    computer.draw_tree_card()  # refresh display
    input('You drew a {}!'.format(chosen_card.common_name))


# gain 1 additional nutrient card for every Conifer in arb
def gain_nutrients(player: Player, times=1):
    time.sleep(0.2)
    print('*** rolling dice ***')
    total_coniferous = len(player.arboretum[Habitat.CONIFER])
    for i in range(times + total_coniferous):
        random_nutrient = Nutrient.random()
        player.nutrients.append(random_nutrient)
        print('{0} rolled a {1}! Adding it to {0}\'s pile of nutrients...'.format(player.name, random_nutrient.value))
        time.sleep(0.3)


def game_status(player: Player):
    time.sleep(0.5)
    print(37 * '<>' + '<')
    if player.arboretum.has_trees():
        print(player.name + '\'s Arboretum:')
        print(player.arboretum.to_string())
        print(75 * "_")
    if player.hand.has_cards():
        print(player.name + '\'s Hand:')
        print(player.hand.to_string())
        print(75 * "_")
    if len(player.nutrients) > 0:
        print(player.name + '\'s Nutrients:')
        print('  {}'.format(list(map(lambda nutrient: nutrient.value, player.nutrients))))
        print(75 * "_")
    print(player.name + '\'s bonus card is: ' + player.bonus.name)
    print(37 * '<>' + '<')


def initialize_game_globals():
    global num_players
    global turns_remaining
    num_players = int(input('Welcome to Wingspan (tree edition)! Enter the number of players (2, 3, or 4): '))
    turns_remaining = num_players * int(input('How many turns would you like to play? '))


def start_game():
    global computer
    global num_players
    global all_players
    global player_1
    global player_2
    global player_3
    global player_4

    # give the computer display 3 cards to start
    # computer.assign_tree_cards()

    # num = int(input('Welcome to Wingspan (tree edition)! Enter the number of players (2, 3, or 4): '))
    # global turns
    # turns = int(input('How many turns would you like to play? '))

    name_1 = input('Player 1, enter your name: ')
    player_1 = Player(1, name_1)
    player_1.assign_bonus_card()

    name_2 = input('Player 2, enter your name: ')
    player_2 = Player(2, name_2)
    player_2.assign_bonus_card()

    all_players = [player_1, player_2]

    if num_players > 2:
        name_3 = input('Player 3, enter your name: ')
        player_3 = Player(3, name_3)
        player_3.assign_bonus_card()
        all_players.append(player_3)

    if num_players > 3:
        name_4 = input('Player 4, enter your name: ')
        player_4 = Player(4, name_4)
        player_4.assign_bonus_card()
        all_players.append(player_4)

    # player_1.assign_tree_cards()
    gain_nutrients(player_1, 3)

    # player_2.assign_tree_cards()
    gain_nutrients(player_2, 3)

    if num_players > 2:
        # player_3.assign_tree_cards()
        gain_nutrients(player_3, 3)

    if num_players > 3:
        # player_4.assign_tree_cards()
        gain_nutrients(player_4, 3)

    time.sleep(1)
    print('\n Setting up the game board...')
    time.sleep(1)
    game_status(player_1)
    time.sleep(1)
    game_status(player_2)
    if num_players > 2:
        time.sleep(1)
        game_status(player_3)
    if num_players > 3:
        time.sleep(1)
        game_status(player_4)
    input('Are you ready to start? Enter any key to begin. ')
    take_a_turn(player_1)


def play_a_card(player: Player):
    global turns_remaining
    choice = input('Select a tree card to play: ')
    tree_card = next(filter(lambda _card: _card.common_name.lower() == choice.lower(), player.hand), None)
    # check for valid input
    if tree_card is not None:
        to_be_removed = []
        print('Checking if you have enough nutrients...')
        for nutrient in tree_card.nutrients:
            if nutrient in player.nutrients:
                to_be_removed.append(nutrient)
            else:
                option = input(
                    'Sorry, you don\'t have enough nutrients to plant that tree.\n' +
                    'Enter (1) to select another tree card, or (2) to go back to the main menu.\n' +
                    '  → ')
                while option != '1' and option != '2':
                    option = input('Invalid input. Enter (1) or (2): ')
                if option == '2':
                    print("Let's try this again.\n")
                    turns_remaining += 1
                    take_a_turn(player)
                if option == '1':
                    play_a_card(player)
                    return
        player.plant_tree(tree_card)
    else:
        option = input("Invalid input. Enter '1' to try again, or '2' to go back to the main menu. \n")
        while option != '1' and option != '2':
            option = input('Invalid input. Enter 1 or 2: ')
        if option == '1':
            play_a_card(player)
        if option == '2':
            print("Let's try this again.\n")
            turns_remaining += 1
            take_a_turn(player)


# hug 1 additional tree for each Deciduous tree in arb
def hug_trees(player: Player):
    total_deciduous = len(player.arboretum[Habitat.DECIDUOUS])
    player.hugs += total_deciduous + 1
    print('You have hugged ' + str(player.hugs) + ' trees <3')


# draw 1 additional tree card for each Urban tree in arb
def draw_tree_cards(player: Player):
    total_urban = len(player.arboretum[Habitat.URBAN])
    for i in range(total_urban + 1):
        print('Select from the following cards:')
        print(computer.hand.to_string())
        print('  4. random card from the deck')
        choice = input('  → ')
        while choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = input('Invalid input. Enter 1, 2, 3, or 4 for a random card: ')
        if choice == '4':  # random card from deck
            player.draw_tree_card()
            print('Drawing random card from deck...')
            input('You drew a ' + str(player.hand[-1].common_name) + "!")
        else:  # 1, 2, or 3 from display
            draw_chosen_card(player.hand, choice)


def switch_players(current_player: Player):  # changes turn between 2 players
    if num_players == 2:
        if current_player.player_id == 1:
            return player_2
        else:
            return player_1
    if num_players == 3:
        if current_player.player_id == 1:
            return player_2
        if current_player.player_id == 2:
            return player_3
        else:
            return player_1
    if num_players == 4:
        if current_player.player_id == 1:
            return player_2
        if current_player.player_id == 2:
            return player_3
        if current_player.player_id == 3:
            return player_4
        else:
            return player_1


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
    print('GAME OVER! Adding up points...')
    time.sleep(0.5)
    global height_list
    global all_players
    for player in all_players:
        height_list.append(player.combined_height)
    # print('height list:')
    # print(height_list)

    scores_1 = get_total_score(player_1)
    scores_2 = get_total_score(player_2)
    # print(scores_1)
    # print(scores_2)

    total_1 = sum(scores_1)
    total_2 = sum(scores_2)

    print(75 * "-")
    time.sleep(0.5)
    print('Step 1: Add up all tree points.')
    print(player_1.name + ' has ' + str(player_1.tree_points) + ' tree points.')
    print(player_2.name + ' has ' + str(player_2.tree_points) + ' tree points.')
    input(75 * "-")
    time.sleep(0.5)
    print('Step 2: Count the number of trees hugged.')
    print(player_1.name + ' has hugged ' + str(player_1.hugs) + ' trees.')
    print(player_2.name + ' has hugged ' + str(player_2.hugs) + ' trees.')
    input(75 * "-")
    time.sleep(0.5)
    print('Step 3: Add up bonus points.')
    print(player_1.name + ', a ' + player_1.bonus.name + ', has earned ' + str(player_1.bonus_points) + ' bonus points.')
    print(player_2.name + ', a ' + player_2.bonus.name + ', has earned ' + str(player_2.bonus_points) + ' bonus points.')
    input(75 * "-")
    time.sleep(0.5)
    print('Final Step: Take the sum of all points.')
    print(75 * "-")
    time.sleep(0.5)
    input('And the winner is...')
    print(player_1.name + ': ' + str(total_1) + ' pts')
    print(player_2.name + ': ' + str(total_2) + ' pts')
    if total_1 > total_2:
        print(player_1.name + '! Congratulations!')
    else:
        print(player_2.name + '! Congratulations!')
    # add lines for players 3 and 4
    return


def take_a_turn(player: Player):
    time.sleep(1)
    global turns_remaining
    global num_players
    print('Turns remaining: ' + str(round(turns_remaining / num_players)))
    turns_remaining -= 1
    print('\n It\'s {}\'s turn!'.format(player.name))
    game_status(player)
    print('\n{}, '.format(player.name), end='')

    move = Move.input_move()
    if move == Move.PLANT_TREE:  # Plant a tree
        play_a_card(player)
    elif move == Move.HUG_TREES:  # Hug a tree
        hug_trees(player)
    elif move == Move.DRAW_NUTRIENTS:  # Gain nutrients
        gain_nutrients(player)
    elif move == Move.DRAW_TREES:  # Draw tree cards
        draw_tree_cards(player)

    game_status(player)
    input('Enter "z" to end your turn. ')
    if turns_remaining > 0:
        take_a_turn(switch_players(player))
    else:
        end_game()


if __name__ == '__main__':
    # welcome_message()
    initialize_game_globals()
    start_game()
