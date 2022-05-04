from typing import NamedTuple, Tuple


class TreeCardData(NamedTuple):
    habitat: str
    scientific_name: str
    common_name: str
    points: int
    height: int
    sun: int
    water: int
    fire: int
    disturbance: int
    michigander: int

    @staticmethod
    def of(tree_card_data: Tuple[str, str, str, int, int, int, int, int, int, int]) -> 'TreeCardData':
        return TreeCardData(*tree_card_data)
