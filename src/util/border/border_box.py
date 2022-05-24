from typing import Final, List, Iterable, Union

from util.ansi import AnsiColor, AnsiFormat
from util.border.border_style import BorderStyle
from util.border.border_box_region import BorderBoxRegion


class BorderBox(List[BorderBoxRegion]):
    width: Final[int] = 80

    def __init__(self: 'BorderBox', regions: Iterable[BorderBoxRegion], color=AnsiColor.DEFAULT,
                 style=BorderStyle.double_standard()) -> None:
        super(BorderBox, self).__init__(regions)
        self.color: Final[AnsiColor] = color
        self.style: Final[BorderStyle] = style

    @staticmethod
    def of(regions: List[Union[str, List[str]]], color=AnsiColor.DEFAULT,
           style=BorderStyle.double_standard()) -> 'BorderBox':
        return BorderBox(map(BorderBoxRegion.of, regions), color, style)

    def draw(self: 'BorderBox') -> str:
        return '{}{}{}'.format(
            self.top_row(),
            self.contents(),
            self.bottom_row(),
        )

    def top_row(self: 'BorderBox') -> str:
        top_left = '{0}{1}'.format(self.style.corner_top_left, self.style.horizontal)
        top_right = '{1}{0}'.format(self.style.corner_top_right, self.style.horizontal)
        top_join = '{1}{0}{1}'.format(self.style.top, self.style.horizontal)

        return self.color.foreground('{}{}{}\n'.format(
            top_left,
            top_join.join([width * self.style.horizontal for width in self[0].row_widths()]),
            top_right,
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
            self.color.foreground(self.style.vertical),
            self.color.foreground(' {} '.format(self.style.inner_vertical))
                .join(self[region_index].row_contents(row)),
        ))

    def content_separator(self: 'BorderBox', region_index: int) -> str:
        above_delimiter_indices = self[region_index].delimiter_indices()
        below_delimiter_indices = self[region_index + 1].delimiter_indices()

        def separator_char(index) -> str:
            return (self.style.inner_cross if (index in below_delimiter_indices) else self.style.inner_bottom) \
                   if (index in above_delimiter_indices) else \
                   (self.style.inner_top if (index in below_delimiter_indices) else self.style.inner_horizontal)

        left = '{0}{1}'.format(self.style.left, self.style.inner_horizontal)
        right = '{1}{0}'.format(self.style.right, self.style.inner_horizontal)
        return self.color.foreground('{}{}{}\n'.format(
            left,
            ''.join(separator_char(index) for index in range(self.width - 4)),
            right,
        ))

    def bottom_row(self: 'BorderBox') -> str:
        bottom_left = '{0}{1}'.format(self.style.corner_bottom_left, self.style.horizontal)
        bottom_right = '{1}{0}'.format(self.style.corner_bottom_right, self.style.horizontal)
        bottom_join = '{1}{0}{1}'.format(self.style.bottom, self.style.horizontal)

        return self.color.foreground('{}{}{}'.format(
            bottom_left,
            bottom_join.join([width * self.style.horizontal for width in self[-1].row_widths()]),
            bottom_right,
        ))


if __name__ == '__main__':
    print(BorderBox.of(['Lorem Ipsum']).draw())

    def random_style() -> BorderStyle:
        random_style.choice += 1
        border_styles = [BorderStyle.standard(), BorderStyle.thick_standard(), BorderStyle.double_standard()]
        return border_styles[random_style.choice % 3]
    random_style.choice = -1

    integrated_format = [
        ['🌞 Lorem Ipsum 🌞', '🌞'],
        '{}\n{}'.format(
            AnsiFormat.fg_blue('Lorem'),
            AnsiFormat.fg_bright_yellow('🌞 Ipsum 🌞'),
        ),
        ['Lorem Ipsum', 'Dolor', 'Sit', 'Amet']
    ]

    for ansi_color in AnsiColor:
        print(BorderBox.of(integrated_format, ansi_color, random_style()).draw())
