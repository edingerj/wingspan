from typing import List, Final, Union, Iterable

from util.ansi import AnsiColor, AnsiFormat
from util.border.border_box_region import BorderBoxRegion


class BorderBox(List[BorderBoxRegion]):
    width: Final[int] = 80

    def __init__(self: 'BorderBox', regions: Iterable[BorderBoxRegion], color=AnsiColor.DEFAULT) -> None:
        super(BorderBox, self).__init__(regions)
        self.color = color

    @staticmethod
    def of(regions: List[Union[str, List[str]]], color=AnsiColor.DEFAULT) -> 'BorderBox':
        return BorderBox(map(BorderBoxRegion.of, regions), color)

    def draw(self: 'BorderBox') -> str:
        return '{}{}{}'.format(
            self.top_row(),
            self.contents(),
            self.bottom_row(),
        )

    def top_row(self: 'BorderBox') -> str:
        return self.color.foreground('╔═{}═╗\n'.format(
            '═╤═'.join([width * '═' for width in self[0].row_widths()]),
        ))

    def contents(self: 'BorderBox') -> str:
        result = ''
        for region_index, region in enumerate(self):
            for row in range(region.rows()):
                result += self.content_line(region_index, row)
            if region_index + 1 < len(self):
                result += self.content_separator(region_index)
        return result

    def content_line(self: 'BorderBox', region_index: int, row: int) -> str:
        return self.color.foreground('{0} {1} {0}\n'.format(
            self.color.foreground('║'),
            self.color.foreground(' │ ').join(self[region_index].row_contents(row)),
        ))

    def content_separator(self: 'BorderBox', region_index: int) -> str:
        above_delimiter_indices = self[region_index].delimiter_indices()
        below_delimiter_indices = self[region_index + 1].delimiter_indices()

        def separator_char(index) -> str:
            return ('┼' if (index in below_delimiter_indices) else '┴') \
                   if (index in above_delimiter_indices) else \
                   ('┬' if (index in below_delimiter_indices) else '─')

        return self.color.foreground('╟─{}─╢\n'.format(
            ''.join(separator_char(index) for index in range(self.width - 4)),
        ))

    def bottom_row(self: 'BorderBox') -> str:
        return self.color.foreground('╚═{}═╝'.format(
            '═╧═'.join([width * '═' for width in self[-1].row_widths()]),
        ))


if __name__ == '__main__':
    print(BorderBox.of(['Lorem Ipsum']).draw())

    integrated_format = [
        ['🌞 Lorem Ipsum 🌞', '🌞'],
        '{}\n{}'.format(
            AnsiFormat.blue('Lorem'),
            AnsiFormat.bright_yellow('🌞 Ipsum 🌞'),
        ),
        ['Lorem Ipsum', 'Dolor', 'Sit', 'Amet']
    ]

    for ansi_color in AnsiColor:
        print(BorderBox.of(integrated_format, ansi_color).draw())
