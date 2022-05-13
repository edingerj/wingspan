from typing import Iterable, List, Union

from util.ansi import visible_offset


class BorderBoxRegion(List[str]):
    def __init__(self: 'BorderBoxRegion', contents: Iterable[str]) -> None:
        super(BorderBoxRegion, self).__init__(contents)

    @staticmethod
    def of(contents: Union[str, List[str]]) -> 'BorderBoxRegion':
        if isinstance(contents, str):
            return BorderBoxRegion([contents])
        elif isinstance(contents, list):
            return BorderBoxRegion(contents)

    def offset(self: 'BorderBoxRegion', column: int = 0, row: int = 0) -> int:
        try:
            line = self[column].split('\n')[row]
            return visible_offset(line)
        except IndexError:
            return 0
