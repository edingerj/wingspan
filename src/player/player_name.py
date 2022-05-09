from typing import Final, List


class PlayerName(str):
    existing_player_names: Final[List['PlayerName']] = []
    max_length: Final[int] = 40

    @staticmethod
    def of(player_name: str) -> 'PlayerName':
        return PlayerName(player_name)

    def valid(self: 'PlayerName') -> bool:
        return self.min_length_validator() & \
               self.max_length_validator() & \
               self.unique_validator()

    def min_length_validator(self: 'PlayerName') -> bool:
        return len(self) > 0

    def max_length_validator(self: 'PlayerName') -> bool:
        return len(self) <= self.max_length

    def unique_validator(self: 'PlayerName') -> bool:
        return self not in self.existing_player_names

    def save(self: 'PlayerName') -> None:
        self.existing_player_names.append(self)
