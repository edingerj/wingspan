from typing import Optional

from gameplay.base.game_main import GameMain


class GameMainWrapper:
    def __init__(self: 'GameMainWrapper') -> None:
        self.__instance = Optional[GameMain]

    def get(self: 'GameMainWrapper') -> GameMain:
        return self.__instance

    def set(self: 'GameMainWrapper', instance: GameMain) -> None:
        self.__instance = instance
