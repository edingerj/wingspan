from player import Player


class GameLoop:
    def __init__(self: 'GameLoop') -> None:
        self.num_players: int = None
        self.total_turns: int = None
        self.turns_remaining: int = None

    def set_num_players(self: 'GameLoop', num_players: int) -> None:
        self.num_players = num_players

    def set_total_turns(self: 'GameLoop', total_turns: int) -> None:
        self.total_turns = total_turns
        self.turns_remaining = self.num_players * self.total_turns
