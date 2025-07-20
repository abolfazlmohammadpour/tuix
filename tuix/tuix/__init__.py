__version__ = "0.0.2"
__author__ = "ABOLFAZL MOHAMMADPOUR"

from tuix.tuix import ESCAPE


from tuix.tuix import BLACK_FOREGROUND, BRIGHT_BLACK_FOREGROUND
from tuix.tuix import RED_FOREGROUND, BRIGHT_RED_FOREGROUND
from tuix.tuix import GREEN_FOREGROUND, BRIGHT_GREEN_FOREGROUND
from tuix.tuix import YELLOW_FOREGROUND, BRIGHT_YELLOW_FOREGROUND
from tuix.tuix import BLUE_FOREGROUND, BRIGHT_BLUE_FOREGROUND
from tuix.tuix import MAGENTA_FOREGROUND, BRIGHT_MAGENTA_FOREGROUND
from tuix.tuix import CYAN_FOREGROUND, BRIGHT_CYAN_FOREGROUND
from tuix.tuix import WHITE_FOREGROUND, BRIGHT_WHITE_FOREGROUND

from tuix.tuix import BLACK_BACKGROUND, BRIGHT_BLACK_BACKGROUND
from tuix.tuix import RED_BACKGROUND, BRIGHT_RED_BACKGROUND
from tuix.tuix import GREEN_BACKGROUND, BRIGHT_GREEN_BACKGROUND
from tuix.tuix import YELLOW_BACKGROUND, BRIGHT_YELLOW_BACKGROUND
from tuix.tuix import BLUE_BACKGROUND, BRIGHT_BLUE_BACKGROUND
from tuix.tuix import MAGENTA_BACKGROUND, BRIGHT_MAGENTA_BACKGROUND
from tuix.tuix import CYAN_BACKGROUND, BRIGHT_CYAN_BACKGROUND
from tuix.tuix import WHITE_BACKGROUND, BRIGHT_WHITE_BACKGROUND


from tuix.tuix import RESET
from tuix.tuix import SET_BOLD, RESET_BOLD
from tuix.tuix import SET_DIM, RESET_DIM
from tuix.tuix import SET_ITALIC, RESET_ITALIC
from tuix.tuix import SET_UNDER_LINE, RESET_UNDER_LINE
from tuix.tuix import SET_BLINK, RESET_BLINK
from tuix.tuix import SET_REVERSE, RESET_REVERSE
from tuix.tuix import SET_HIDE, RESET_HIDE
from tuix.tuix import SET_STRIKE_LINE, RESET_STRIKE_LINE


from tuix.tuix import change_background_color, change_foreground_color


from tuix.tuix import reset_format
from tuix.tuix import set_bold_format, reset_bold_format
from tuix.tuix import set_dim_format, reset_dim_format
from tuix.tuix import set_italic_format, reset_italic_format
from tuix.tuix import set_under_line_format, reset_under_line_format
from tuix.tuix import set_blink_format, reset_blink_format
from tuix.tuix import set_reverse_format, reset_reverse_format
from tuix.tuix import set_hide_format, reset_hide_format
from tuix.tuix import set_strike_line_format, reset_strike_line_format


__all__ = [
    "ESCAPE",
]

__all__ += [
    "BLACK_FOREGROUND", "BRIGHT_BLACK_FOREGROUND",
    "RED_FOREGROUND", "BRIGHT_RED_FOREGROUND",
    "GREEN_FOREGROUND", "BRIGHT_GREEN_FOREGROUND",
    "YELLOW_FOREGROUND", "BRIGHT_YELLOW_FOREGROUND",
    "BLUE_FOREGROUND", "BRIGHT_BLUE_FOREGROUND",
    "MAGENTA_FOREGROUND", "BRIGHT_MAGENTA_FOREGROUND",
    "CYAN_FOREGROUND", "BRIGHT_CYAN_FOREGROUND",
    "WHITE_FOREGROUND", "BRIGHT_WHITE_FOREGROUND",
]

__all__ += [
    "BLACK_BACKGROUND", "BRIGHT_BLACK_BACKGROUND",
    "RED_BACKGROUND", "BRIGHT_RED_BACKGROUND",
    "GREEN_BACKGROUND", "BRIGHT_GREEN_BACKGROUND",
    "YELLOW_BACKGROUND", "BRIGHT_YELLOW_BACKGROUND",
    "BLUE_BACKGROUND", "BRIGHT_BLUE_BACKGROUND",
    "MAGENTA_BACKGROUND", "BRIGHT_MAGENTA_BACKGROUND",
    "CYAN_BACKGROUND", "BRIGHT_CYAN_BACKGROUND",
    "WHITE_BACKGROUND", "BRIGHT_WHITE_BACKGROUND"
]

__all__ += [
    "RESET",
    "SET_BOLD", "RESET_BOLD",
    "SET_DIM", "RESET_DIM",
    "SET_ITALIC", "RESET_ITALIC",
    "SET_UNDER_LINE", "RESET_UNDER_LINE",
    "SET_BLINK", "RESET_BLINK",
    "SET_REVERSE", "RESET_REVERSE",
    "SET_HIDE", "RESET_HIDE",
    "SET_STRIKE_LINE", "RESET_STRIKE_LINE"
]
__all__ += [
    "change_foreground_color",
    "change_background_color"
]

__all__ += [
    "reset_format",
    "set_bold_format", "reset_bold_format",
    "set_dim_format", "reset_dim_format",
    "set_italic_format", "reset_italic_format",
    "set_under_line_format", "reset_under_line_format",
    "set_blink_format", "reset_blink_format",
    "set_reverse_format", "reset_reverse_format",
    "set_hide_format", "reset_hide_format",
    "set_strike_line_format", "reset_strike_line_format"
]
