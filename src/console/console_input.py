from game import Move
from player import Hand, Player


def get_move(player: Player) -> Move:
    move_string = input_move(player)
    move = Move.from_string(move_string)
    while move is None:
        print('Invalid Move: {}. Please try again.'.format(move_string))
        move_string = input_move(player)
        move = Move.from_string(move_string)
    return move


def input_move(player: Player) -> str:
    return input(
        '{}, select from the following options:\n'.format(player.name) +
        '  1. Plant a tree\n' +
        '  2. Hug some trees\n' +
        '  3. Draw nutrients\n' +
        '  4. Draw tree cards\n' +
        '  5. Skip your turn\n'
        '  → ')


def input_retry_plant_tree() -> int:
    choice = input(
        '  1. Plant another tree card\n' +
        '  2. Go back to the main menu\n' +
        '  → ')
    while choice not in ('1', '2'):
        choice = input(
            'Invalid input: {}. Enter (1) or (2):\n'.format(choice) +
            '  → ')
    return int(choice)


def select_plant_tree_card(hand: Hand) -> int:
    choice = input_plant_tree_card(hand)
    choice_index = hand.index_of(choice)
    if choice_index is None:
        print('You don\'t have a {} in your hand.'.format(choice))
    return choice_index


def input_plant_tree_card(hand: Hand) -> str:
    return input(
        'You may plant one of the following tree cards:\n' +
        '{}\n'.format(hand.to_string()) +
        '  → ')


def select_draw_tree_card(displayed_tree_cards: Hand) -> int:
    choice = input_draw_tree_card(displayed_tree_cards)
    choice_index = displayed_tree_cards.index_of(choice, include_random=True)
    while choice_index not in range(len(displayed_tree_cards) + 2):
        choice = input(
            'Invalid tree selection: {}. Please try again:\n'.format(choice) +
            '  → ')
        choice_index = displayed_tree_cards.index_of(choice, include_random=True)
    return choice_index


def input_draw_tree_card(displayed_tree_cards: Hand) -> str:
    return input(
        'You may draw one of the following tree cards:\n' +
        '{}\n'.format(displayed_tree_cards.to_string()) +
        '  {}. random card from the deck\n'.format(len(displayed_tree_cards) + 1) +
        '  → ')


__all__ = [
    'get_move',
    'input_retry_plant_tree',
    'select_plant_tree_card',
    'select_draw_tree_card',
]


if __name__ == '__main__':
    _player = Player('Seb', None)
    print(get_move(_player))
