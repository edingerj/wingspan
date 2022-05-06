from typing import Final, List, Optional

from bonus import Bonus
from player import Player


class BonusApplicator:
    def __init__(self: 'BonusApplicator', all_players: List[Player]) -> None:
        self.all_players: Final[List[Player]] = all_players

    def apply_bonuses(self: 'BonusApplicator') -> None:
        self.apply_bonus(Bonus.TALLEST_ARBORETUM, self.get_tallest_arboretum_player())
        self.apply_bonus(Bonus.LARGEST_ARBORETUM, self.get_largest_arboretum_player())
        self.apply_bonus(Bonus.MOST_TREES_HUGGED, self.get_most_trees_hugged_player())

    def apply_bonus(self: 'BonusApplicator', bonus: Bonus, bonus_player: Optional[Player]) -> None:
        if bonus_player is not None:
            for player in self.all_players:
                if bonus in player.bonuses:
                    player.bonuses.remove(bonus)
            bonus_player.bonuses.append(bonus)

    # Todo: check for duplicate max values
    #  and in the case of bonus_value tie,
    #  return the same player as currently
    #  holds the bonus.
    def get_tallest_arboretum_player(self: 'BonusApplicator') -> Optional[Player]:
        combined_tree_heights = [player.arboretum.get_total_height() for player in self.all_players]
        if max(combined_tree_heights) == 0:
            return None
        else:
            return self.all_players[combined_tree_heights.index(max(combined_tree_heights))]

    # Todo: check for duplicate max values
    #  and in the case of bonus_value tie,
    #  return the same player as currently
    #  holds the bonus.
    def get_largest_arboretum_player(self: 'BonusApplicator') -> Optional[Player]:
        arboretum_sizes = [len(player.arboretum.get_all_trees()) for player in self.all_players]
        if max(arboretum_sizes) == 0:
            return None
        else:
            return self.all_players[arboretum_sizes.index(max(arboretum_sizes))]

    # Todo: check for duplicate max values
    #  and in the case of bonus_value tie,
    #  return the same player as currently
    #  holds the bonus.
    def get_most_trees_hugged_player(self: 'BonusApplicator') -> Optional[Player]:
        trees_hugged = [player.hugs for player in self.all_players]
        if max(trees_hugged) == 0:
            return None
        else:
            return self.all_players[trees_hugged.index(max(trees_hugged))]