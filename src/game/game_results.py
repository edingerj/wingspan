from typing import List

from player import Player


class GameResults:
    def __init__(self: 'GameResults', all_players: List[Player]) -> None:
        self.all_players = all_players
        self.player_scores = self.get_player_scores()
        self.winning_player = self.get_winning_player()

    def get_player_scores(self: 'GameResults') -> List[int]:
        return [player.get_total_score() for player in self.all_players]

    def get_winning_player(self: 'GameResults') -> Player:
        max_score = max(self.player_scores)
        return self.all_players[self.player_scores.index(max_score)]
