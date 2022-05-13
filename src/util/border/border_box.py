from typing import List, Final, Union, Iterable

from util.ansi import AnsiFormat, visible_offset
from util.border.border_box_region import BorderBoxRegion


class BorderBox(List[BorderBoxRegion]):
    width: Final[int] = 80

    def __init__(self: 'BorderBox', regions: Iterable[BorderBoxRegion]) -> None:
        super(BorderBox, self).__init__(regions)

    @staticmethod
    def of(regions: List[Union[str, List[str]]]) -> 'BorderBox':
        return BorderBox(map(BorderBoxRegion.of, regions))

    def draw(self: 'BorderBox') -> str:
        result = AnsiFormat.bright_black('╔{}╗\n'.format((self.width - 2) * '═'))

        for index, region in enumerate(self):
            for column in region:
                for line in column.split('\n'):
                    result += '{0} {1} {0}\n'.format(
                        AnsiFormat.bright_black('║'),
                        '{}'.format(line).ljust(self.width - visible_offset(line) - 4),
                    )
            if index + 1 < len(self):
                result += AnsiFormat.bright_black('╟{}╢\n'.format((self.width - 2) * '─'))
        result += AnsiFormat.bright_black('╚{}╝\n'.format((self.width - 2) * '═'))
        return result


if __name__ == '__main__':
    print(BorderBox.of(['reee']).draw())
    print(BorderBox.of(['🌞', AnsiFormat.blue('reee\n🌞🌞')]).draw())
