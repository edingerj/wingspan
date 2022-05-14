from typing import List, Iterable, Optional

from player.player_color import PlayerColor


class PlayerColors(List[PlayerColor]):
    def __init__(self: 'PlayerColors', colors: Iterable[PlayerColor] = ()):
        super(PlayerColors, self).__init__(colors)

    @staticmethod
    def all() -> 'PlayerColors':
        return PlayerColors(PlayerColor)

    # where choice can be a color name, or a 1 index
    def index_of(self: 'PlayerColors', choice: str) -> Optional[int]:
        player_color: Optional[PlayerColor] = \
            next(filter(lambda color: color.value.lower() == choice.lower(), self), None)
        if player_color is not None:
            return self.index(player_color)
        try:
            index = int(choice) - 1
            return index if (index < len(self)) else None
        except ValueError:
            return None

    def table_format(self: 'PlayerColors') -> str:
        return '\n'.join(['  {} {}'.format(
            '{}.'.format(index + 1).ljust(3),
            '{}'.format(player_color.color_format()),
        ) for index, player_color in enumerate(self)])


if __name__ == '__main__':
    player_colors = PlayerColors.all()
    print(player_colors.table_format())
