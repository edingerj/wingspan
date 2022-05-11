from typing import Optional, TypeVar

from game.runtime_flags import RuntimeFlags


T = TypeVar('T', bound=RuntimeFlags)


class RuntimeFlagsWrapper:
    def __init__(self: 'RuntimeFlagsWrapper') -> None:
        self.__instance = Optional[T]

    def get(self: 'RuntimeFlagsWrapper') -> T:
        return self.__instance

    def set(self: 'RuntimeFlagsWrapper', instance: T) -> None:
        self.__instance = instance
