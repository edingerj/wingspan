from typing import Iterable, List, Union, Final

from util.terminal.cursor import VisibleText


class BorderBoxRegion(List[str]):
    max_width: Final[int] = 80

    def __init__(self: 'BorderBoxRegion', contents: Iterable[str]) -> None:
        super(BorderBoxRegion, self).__init__(contents)

    @staticmethod
    def of(contents: Union[str, List[str]]) -> 'BorderBoxRegion':
        if isinstance(contents, str):
            return BorderBoxRegion([contents])
        elif isinstance(contents, list):
            return BorderBoxRegion(contents)

    def rows(self: 'BorderBoxRegion') -> int:
        return max([len(column.split('\n')) for column in self])

    def row_contents(self: 'BorderBoxRegion', row: int) -> List[str]:
        return [self.grid_contents(row, column) for column in range(len(self))]

    def grid_contents(self: 'BorderBoxRegion', row: int, column: int) -> str:
        grid_width = self.row_widths()[column]
        try:
            line = self[column].split('\n')[row]
            return line.ljust(grid_width - self.grid_offset(row, column))
        except IndexError:
            return ' ' * grid_width

    def delimiter_indices(self: 'BorderBoxRegion') -> List[int]:
        widths = self.row_widths()
        indices = []
        for column in range(1, len(widths)):
            indices.append(sum(widths[:column]) + 1 + max(0, 3 * (column - 1)))
        return indices

    def row_widths(self: 'BorderBoxRegion') -> List[int]:
        if len(self) == 1:
            return [self.max_width - 4]
        else:
            row_widths = [self.row_width(column) for column in range(len(self))]
            row_widths[0] = max(row_widths[0], self.max_width - 4 - sum(row_widths[1:]) - (3 * len(row_widths[1:])))
            return row_widths

    def row_width(self: 'BorderBoxRegion', column: int) -> int:
        return max([
            VisibleText.length(line) for line in self[column].split('\n')
        ])

    def grid_offset(self: 'BorderBoxRegion', row: int, column: int) -> int:
        try:
            line = self[column].split('\n')[row]
            return VisibleText.offset(line)
        except IndexError:
            return 0
