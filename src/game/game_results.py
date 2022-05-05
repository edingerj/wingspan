from typing import List, Optional

from player import Player


class GameResults:
    def __init__(self: 'GameResults', all_players: List[Player]) -> None:
        self.all_players = all_players
        self.combined_tree_heights = self.get_combined_tree_heights()
        self.tallest_arboretum_player = self.get_tallest_arboretum_player()
        self.player_scores = self.get_player_scores()
        self.winning_player = self.get_winning_player()

    def get_combined_tree_heights(self: 'GameResults') -> List[int]:
        return [player.arboretum.get_total_height() for player in self.all_players]

    def get_tallest_arboretum_player(self: 'GameResults') -> Optional[Player]:
        max_height = max(self.combined_tree_heights)
        if max_height == 0:
            return None
        return self.all_players[self.combined_tree_heights.index(max_height)]

    def get_player_scores(self: 'GameResults') -> List[int]:
        return [self.get_player_score(player) for player in self.all_players]

    def get_player_score(self: 'GameResults', player: Player) -> int:
        has_tallest_arboretum = player == self.tallest_arboretum_player
        return player.get_total_score(has_tallest_arboretum)

    def get_winning_player(self: 'GameResults') -> Player:
        max_score = max(self.player_scores)
        return self.all_players[self.player_scores.index(max_score)]
