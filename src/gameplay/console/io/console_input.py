from gameplay.base.io import Info, Move, TurnPhase
from gameplay.console.io.console_util import clear_lines
from player import Hand, Player


def get_information(player: Player, turn_phase: TurnPhase) -> Info:
    info_string = input_information(player, turn_phase)
    info = Info.from_string(info_string)
    clear_lines(6)
    while info is None:
        print('Invalid Display Option: {}. Please try again.'.format(info_string))
        info_string = input_information(player, turn_phase)
        clear_lines(7)
        info = Info.from_string(info_string)
    return info


def input_information(player: Player, turn_phase: TurnPhase) -> str:
    return input(
        '{}, select from the following options:\n'.format(player.name) +
        '  1. Display your hand\n' +
        '  2. Display the top of the deck\n' +
        '  3. Display your bonuses\n' +
        '  4. {}\n'.format(turn_phase.get_continue_information_text()) +
        '  → ').strip()


def get_move(player: Player) -> Move:
    move_string = input_move(player)
    move = Move.from_string(move_string)
    clear_lines(7)
    while move is None:
        print('Invalid Move: {}. Please try again.'.format(move_string))
        move_string = input_move(player)
        move = Move.from_string(move_string)
        clear_lines(8)
    return move


# Todo: specify how many of each action you will perform
#  based on which habitat of trees you are selecting from
def input_move(player: Player) -> str:
    return input(
        '{}, select from the following options:\n'.format(player.name) +
        '  1. Plant a tree\n' +
        '  2. Hug some trees\n' +
        '  3. Draw nutrients\n' +
        '  4. Draw tree cards\n' +
        '  5. Skip your move\n'
        '  → ').strip()


def input_retry_plant_tree() -> int:
    choice = input(
        '  1. Plant another tree card\n' +
        '  2. Go back to the main menu\n' +
        '  → ').strip()
    while choice not in ('1', '2'):
        choice = input(
            'Invalid input: {}. Enter (1) or (2):\n'.format(choice) +
            '  → ').strip()
        clear_lines(2)
    clear_lines(4)  # accounts for the "You don't have a {}" or "You don't have enough nutrients to plant a {}" line
    return int(choice)


def select_plant_tree_card(hand: Hand) -> int:
    choice = input_plant_tree_card(hand)
    choice_index = hand.index_of(choice)
    clear_lines(len(hand) + 2)
    if choice_index is None:
        print('You don\'t have a {} in your hand.'.format(choice))
    return choice_index


def input_plant_tree_card(hand: Hand) -> str:
    return input(
        'You may plant one of the following tree cards:\n' +
        '{}\n'.format(hand.table_format()) +
        '  → ').strip()


def input_draw_tree_card_index(displayed_tree_cards: Hand) -> int:
    choice = input_draw_tree_card(displayed_tree_cards)
    choice_index = displayed_tree_cards.index_of(choice, include_random=True)
    while choice_index not in range(len(displayed_tree_cards) + 2):
        choice = retry_input_draw_tree_card(choice)
        choice_index = displayed_tree_cards.index_of(choice, include_random=True)
        clear_lines(2)
    clear_lines(len(displayed_tree_cards) + 3)
    return choice_index


def input_draw_tree_card(displayed_tree_cards: Hand) -> str:
    return input(
        'You may draw one of the following tree cards:\n' +
        '{}\n'.format(displayed_tree_cards.table_format()) +
        '  {}.  random card from the deck\n'.format(len(displayed_tree_cards) + 1) +
        '  → ').strip()


def retry_input_draw_tree_card(previous_choice: str) -> str:
    return input(
        'Invalid tree selection: {}. Please try again:\n'.format(previous_choice) +
        '  → ').strip()


__all__ = [
    'get_information',
    'get_move',
    'input_retry_plant_tree',
    'select_plant_tree_card',
    'input_draw_tree_card_index',
]


if __name__ == '__main__':
    _player = Player('Seb', None, None)
    print(get_move(_player))
