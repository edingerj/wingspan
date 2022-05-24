from typing import Final

from util.border.border_characters import *


class BorderStyle:
    def __init__(self: 'BorderStyle', horizontal: str, vertical: str, left: str, right: str, top: str, bottom: str,
                 corner_top_left: str, corner_top_right: str, corner_bottom_left: str, corner_bottom_right: str,
                 inner_horizontal: str, inner_vertical: str, inner_cross: str,
                 inner_left: str, inner_right: str, inner_top: str, inner_bottom: str) -> None:
        self.horizontal: Final[str] = horizontal
        self.vertical: Final[str] = vertical
        self.left: Final[str] = left
        self.right: Final[str] = right
        self.top: Final[str] = top
        self.bottom: Final[str] = bottom
        self.corner_top_left: Final[str] = corner_top_left
        self.corner_top_right: Final[str] = corner_top_right
        self.corner_bottom_left: Final[str] = corner_bottom_left
        self.corner_bottom_right: Final[str] = corner_bottom_right
        self.inner_horizontal: Final[str] = inner_horizontal
        self.inner_vertical: Final[str] = inner_vertical
        self.inner_cross: Final[str] = inner_cross
        self.inner_left: Final[str] = inner_left
        self.inner_right: Final[str] = inner_right
        self.inner_top: Final[str] = inner_top
        self.inner_bottom: Final[str] = inner_bottom

    @staticmethod
    def standard() -> 'BorderStyle':
        return BorderStyle(
            STANDARD_HORIZONTAL,
            STANDARD_VERTICAL,
            STANDARD_JOIN_LEFT,
            STANDARD_JOIN_RIGHT,
            STANDARD_JOIN_TOP,
            STANDARD_JOIN_BOTTOM,
            STANDARD_CORNER_TOP_LEFT,
            STANDARD_CORNER_TOP_RIGHT,
            STANDARD_CORNER_BOTTOM_LEFT,
            STANDARD_CORNER_BOTTOM_RIGHT,
            STANDARD_HORIZONTAL,
            STANDARD_VERTICAL,
            STANDARD_JOIN_CROSS,
            STANDARD_JOIN_LEFT,
            STANDARD_JOIN_RIGHT,
            STANDARD_JOIN_TOP,
            STANDARD_JOIN_BOTTOM,
        )

    @staticmethod
    def thick_standard() -> 'BorderStyle':
        return BorderStyle(
            THICK_HORIZONTAL,
            THICK_VERTICAL,
            THICK_STANDARD_JOIN_LEFT,
            THICK_STANDARD_JOIN_RIGHT,
            THICK_STANDARD_JOIN_TOP,
            THICK_STANDARD_JOIN_BOTTOM,
            THICK_CORNER_TOP_LEFT,
            THICK_CORNER_TOP_RIGHT,
            THICK_CORNER_BOTTOM_LEFT,
            THICK_CORNER_BOTTOM_RIGHT,
            STANDARD_HORIZONTAL,
            STANDARD_VERTICAL,
            STANDARD_JOIN_CROSS,
            STANDARD_JOIN_LEFT,
            STANDARD_JOIN_RIGHT,
            STANDARD_JOIN_TOP,
            STANDARD_JOIN_BOTTOM,
        )

    @staticmethod
    def double_standard() -> 'BorderStyle':
        return BorderStyle(
            DOUBLE_HORIZONTAL,
            DOUBLE_VERTICAL,
            DOUBLE_STANDARD_JOIN_LEFT,
            DOUBLE_STANDARD_JOIN_RIGHT,
            DOUBLE_STANDARD_JOIN_TOP,
            DOUBLE_STANDARD_JOIN_BOTTOM,
            DOUBLE_CORNER_TOP_LEFT,
            DOUBLE_CORNER_TOP_RIGHT,
            DOUBLE_CORNER_BOTTOM_LEFT,
            DOUBLE_CORNER_BOTTOM_RIGHT,
            STANDARD_HORIZONTAL,
            STANDARD_VERTICAL,
            STANDARD_JOIN_CROSS,
            STANDARD_JOIN_LEFT,
            STANDARD_JOIN_RIGHT,
            STANDARD_JOIN_TOP,
            STANDARD_JOIN_BOTTOM,
        )
