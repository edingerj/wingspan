from abc import ABC
from typing import List

from console.console_input import get_move
from console.sleep import sleep
from game import GameMain
from player import Player
from tree import Habitat, TreeCard


class ConsoleGameMain(GameMain, ABC):
    def __init__(self: 'ConsoleGameMain', all_players: List[Player], total_turns: int) -> None:
        super(ConsoleGameMain, self).__init__(all_players, total_turns)

    def take_turn(self: 'ConsoleGameMain', player: Player) -> None:
        sleep(0.5)
        print('Turns remaining: ' + str(round(self.turns_remaining / len(self.all_players))))
        self.turns_remaining -= 1

        print('\nIt\'s {}\'s turn!'.format(player.name))
        print(player.to_string())
        print('{}, '.format(player.name), end='')

        move = get_move()
        self.do_move(player, move)
        print(player.to_string())

        input('Enter "z" to end your turn. ')
        if self.turns_remaining > 0:
            self.take_turn(self.get_next_player(player))
        else:
            self.end_game()

    def retry_turn(self: 'ConsoleGameMain', player: Player) -> None:
        print("Let's try this again...\n")
        sleep(0.5)
        super(ConsoleGameMain, self).retry_turn(player)

    def plant_tree(self: 'ConsoleGameMain', player: Player) -> None:
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
                self.retry_plant_tree(player)
        else:
            print('You don\'t have a {} in your hand.'.format(choice))
            self.retry_plant_tree(player)

    def retry_plant_tree(self: 'ConsoleGameMain', player: Player) -> None:
        option = input(
            '  1. Select another tree card\n'
            '  2. Go back to the main menu\n' +
            '  → ')
        while option != '1' and option != '2':
            option = input('Invalid input. Enter (1) or (2): ')
        if option == '1':
            self.plant_tree(player)
        if option == '2':
            self.retry_turn(player)

    # hug 1 additional tree for each Deciduous tree in arb
    def hug_trees(self: 'ConsoleGameMain', player: Player) -> None:
        sleep(0.2)
        hugs = player.hug_trees()
        print('*** hugging {} tree{} ***'.format(hugs, 's' if (hugs != 1) else ''))
        sleep(0.2)
        print('  {} has hugged {} trees <3'.format(player.name, player.hugs))

    # gain 1 additional nutrient card for every Conifer tree in arb
    def draw_nutrient_cards(self: 'ConsoleGameMain', player: Player) -> None:
        sleep(0.2)
        nutrients = player.draw_nutrient_cards()
        print('*** rolling {} dice ***'.format(len(nutrients)))
        for nutrient in nutrients:
            sleep(0.2)
            print('  {0} rolled a {1}! Adding it to {0}\'s pile of nutrients...'
                  .format(player.name, nutrient.to_emoji()))

    # draw 1 additional tree card for each Urban tree in arb
    def draw_tree_cards(self: 'ConsoleGameMain', player: Player) -> None:
        total_urban = len(player.arboretum[Habitat.URBAN])
        for i in range(total_urban + 1):
            choice = int(input(
                'Select from the following cards:\n' +
                '{}\n'.format(self.computer.hand.to_string()) +
                '  4. random card from the deck\n'
                '  → '))
            while choice not in range(1, 5):
                choice = int(input(
                    'Invalid input. Enter 1, 2, 3, or 4 for a random card:\n' +
                    '  → '))
            if choice in range(1, 4):
                self.draw_chosen_tree_card(player, choice)
            elif choice == 4:
                self.draw_random_tree_card(player)

    def draw_chosen_tree_card(self: 'ConsoleGameMain', player: Player, choice: int) -> None:
        tree_card = super(ConsoleGameMain, self).draw_chosen_tree_card(player, choice)
        print('You drew a {}!'.format(tree_card.common_name))

    def draw_random_tree_card(self: 'ConsoleGameMain', player: Player) -> None:
        print('Drawing random card from deck...')
        tree_card = super(ConsoleGameMain, self).draw_random_tree_card(player)
        print('You drew a {}!'.format(tree_card.common_name))

    def end_game(self: 'ConsoleGameMain') -> None:
        results = self.get_results()
        print('\n*** GAME OVER ***\nAdding up points...')
        sleep(0.5)
        print(75 * "-")
        sleep(0.5)

        print('Step 1: Add up all tree points.')
        for player in self.all_players:
            print('  {} has earned {} tree points.'.format(player.name, player.tree_points))
        input(75 * "-")
        sleep(0.5)

        print('Step 2: Count the number of trees hugged.')
        for player in self.all_players:
            print('  {} has hugged {} trees.'.format(player.name, player.hugs))
        input(75 * "-")
        sleep(0.5)

        print('Step 3: Add up bonus points.')
        for player in self.all_players:
            print('  {}, a {}, has earned {} bonus points.'.format(player.name, player.bonus.name, player.bonus_points))
        input(75 * "-")
        sleep(0.5)

        print('Final Step: Take the sum of all points.')
        print(75 * "-")
        sleep(0.5)

        input('And the winner is...')
        print('\n{}! Congratulations!'.format(results.winning_player.name))

        print('\nTotal Points:')
        for index, player in enumerate(self.all_players):
            print('  {}: {} pts'.format(player.name, results.player_scores[index]))
