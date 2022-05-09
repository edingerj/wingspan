from abc import ABCMeta

from game.display_format import DisplayFormat


class RuntimeFlags(metaclass=ABCMeta):
    def __init__(
            self: 'RuntimeFlags',
            display_format: DisplayFormat,
            experimental: bool,
    ):
        self.display_format = display_format
        self.experimental = experimental
