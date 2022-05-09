from typing import List

from player.player import Player
from player.player_name import PlayerName


class Players(List[Player]):
    def next(self: 'Players', current_player: Player) -> Player:
        player_index = self.index(current_player)
        return self[0] if (player_index == len(self) - 1) else self[player_index + 1]

    def get_player_scores(self: 'Players') -> List[int]:
        return [player.get_total_score() for player in self]

    def get_ranked_player_scores(self: 'Players') -> List[int]:
        ranked_player_scores = list(set(self.get_player_scores()))
        ranked_player_scores.sort(reverse=True)
        return ranked_player_scores

    def get_players_by_score(self: 'Players', score: int) -> List[Player]:
        player_scores = self.get_player_scores()
        return [self[index] for index in range(len(player_scores)) if player_scores[index] == score]

    def get_winning_players(self: 'Players') -> List[Player]:
        max_player_scores = max(self.get_player_scores())
        return self.get_players_by_score(max_player_scores)

    def score_board_format(self: 'Players') -> str:
        result = ''
        place = 1
        for score in self.get_ranked_player_scores():
            players = self.get_players_by_score(score)
            for player in players:
                result += '  {}. {} │ {}\n'.format(
                    place,
                    player.name.ljust(PlayerName.max_length),
                    '{} pts'.format(score),
                )
            place += len(players)
        return result
