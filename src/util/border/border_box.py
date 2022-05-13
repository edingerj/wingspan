from typing import List, Final, Union, Iterable

from util.ansi import AnsiColor, AnsiFormat, visible_offset
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
        result = self.color.foreground('╔{}╗\n'.format((self.width - 2) * '═'))

        for index, region in enumerate(self):
            for column in region:
                for line in column.split('\n'):
                    result += '{0} {1} {0}\n'.format(
                        self.color.foreground('║'),
                        '{}'.format(line).ljust(self.width - visible_offset(line) - 4),
                    )
            if index + 1 < len(self):
                result += self.color.foreground('╟{}╢\n'.format((self.width - 2) * '─'))

        result += self.color.foreground('╚{}╝'.format((self.width - 2) * '═'))
        return result


if __name__ == '__main__':
    print(BorderBox.of(['Lorem Ipsum']).draw())

    integrated_format = ['🌞 Lorem Ipsum 🌞', '{}\n{}'.format(
        AnsiFormat.blue('Lorem'),
        AnsiFormat.bright_yellow('🌞 Ipsum 🌞'),
    )]

    for ansi_color in AnsiColor:
        print(BorderBox.of(integrated_format, ansi_color).draw())
