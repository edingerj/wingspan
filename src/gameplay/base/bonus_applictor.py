from typing import Final, Optional, List

from bonus import BonusToken
from player import Player, Players


class BonusApplicator:
    def __init__(self: 'BonusApplicator', players: Players) -> None:
        self.players: Final[Players] = players

    def apply_bonuses(self: 'BonusApplicator') -> None:
        self.apply_bonus(BonusToken.TALLEST_ARBORETUM, self.get_player_arboretum_heights())
        self.apply_bonus(BonusToken.LARGEST_ARBORETUM, self.get_player_arboretum_sizes())
        self.apply_bonus(BonusToken.MOST_TREES_HUGGED, self.get_player_trees_hugged())

    def apply_bonus(self: 'BonusApplicator', bonus: BonusToken, bonus_values: List[int]) -> None:
        bonus_player = self.get_next_bonus_player(bonus, bonus_values)
        if bonus_player is not None:
            for player in self.players:
                if bonus in player.bonuses:
                    player.bonuses.remove(bonus)
            bonus_player.bonuses.append(bonus)

    # region get next bonus player
    def get_next_bonus_player(self: 'BonusApplicator', bonus: BonusToken, bonus_values: List[int]) -> Optional[Player]:
        applicable_players = self.get_applicable_bonus_players(bonus_values)
        current_player = self.get_current_bonus_player(bonus)
        if max(bonus_values) == 0:
            return None
        elif current_player in applicable_players:
            return current_player
        else:
            return applicable_players[0]

    def get_applicable_bonus_players(self: 'BonusApplicator', bonus_values: List[int]) -> List[Player]:
        return [self.players[index] for index in range(len(bonus_values)) if bonus_values[index] == max(bonus_values)]

    def get_current_bonus_player(self: 'BonusApplicator', bonus: BonusToken) -> Optional[Player]:
        return next(filter(lambda player: bonus in player.bonuses, self.players), None)
    # endregion get next bonus player

    # region get player bonus values
    def get_player_arboretum_heights(self: 'BonusApplicator') -> List[int]:
        return [player.arboretum.get_total_height() for player in self.players]

    def get_player_arboretum_sizes(self: 'BonusApplicator') -> List[int]:
        return [len(player.arboretum.get_all_trees()) for player in self.players]

    def get_player_trees_hugged(self: 'BonusApplicator') -> List[int]:
        return [player.hugs for player in self.players]
    # endregion get player bonus values
