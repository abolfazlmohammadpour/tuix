from .escape_code import ESCAPE


from .color_code import BLACK_FOREGROUND, BRIGHT_BLACK_FOREGROUND
from .color_code import RED_FOREGROUND, BRIGHT_RED_FOREGROUND
from .color_code import GREEN_FOREGROUND, BRIGHT_GREEN_FOREGROUND
from .color_code import YELLOW_FOREGROUND, BRIGHT_YELLOW_FOREGROUND
from .color_code import BLUE_FOREGROUND, BRIGHT_BLUE_FOREGROUND
from .color_code import MAGENTA_FOREGROUND, BRIGHT_MAGENTA_FOREGROUND
from .color_code import CYAN_FOREGROUND, BRIGHT_CYAN_FOREGROUND
from .color_code import WHITE_FOREGROUND, BRIGHT_WHITE_FOREGROUND

from .color_code import BLACK_BACKGROUND, BRIGHT_BLACK_BACKGROUND
from .color_code import RED_BACKGROUND, BRIGHT_RED_BACKGROUND
from .color_code import GREEN_BACKGROUND, BRIGHT_GREEN_BACKGROUND
from .color_code import YELLOW_BACKGROUND, BRIGHT_YELLOW_BACKGROUND
from .color_code import BLUE_BACKGROUND, BRIGHT_BLUE_BACKGROUND
from .color_code import MAGENTA_BACKGROUND, BRIGHT_MAGENTA_BACKGROUND
from .color_code import CYAN_BACKGROUND, BRIGHT_CYAN_BACKGROUND
from .color_code import WHITE_BACKGROUND, BRIGHT_WHITE_BACKGROUND


from .format_code import RESET
from .format_code import SET_BOLD, RESET_BOLD
from .format_code import SET_DIM, RESET_DIM
from .format_code import SET_ITALIC, RESET_ITALIC
from .format_code import SET_UNDER_LINE, RESET_UNDER_LINE
from .format_code import SET_BLINK, RESET_BLINK
from .format_code import SET_REVERSE, RESET_REVERSE
from .format_code import SET_HIDE, RESET_HIDE
from .format_code import SET_STRIKE_LINE, RESET_STRIKE_LINE


def change_foreground_color(color_code: str) -> None:
    """
        This Function Will Change The Foreground Color Of The Terminal,
        That Just Support Standard Color.
        All Of Standard Colors Supported By This Function Are:
        {Black, Red, Green, Yellow, Blue, Magenta, Cyan, White
        Bright Black, Bright Red, Bright Green, Bright Yellow,
        Bright Blue, Bright Magenta, Bright Cyan, Bright White}
    """
    if color_code == BLACK_FOREGROUND:
        print(f"{ESCAPE}{BLACK_FOREGROUND}", end="")
    elif color_code == BRIGHT_BLACK_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_BLACK_FOREGROUND}", end="")
    elif color_code == RED_FOREGROUND:
        print(f"{ESCAPE}{RED_FOREGROUND}", end="")
    elif color_code == BRIGHT_RED_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_RED_FOREGROUND}", end="")
    elif color_code == GREEN_FOREGROUND:
        print(f"{ESCAPE}{GREEN_FOREGROUND}", end="")
    elif color_code == BRIGHT_GREEN_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_GREEN_FOREGROUND}", end="")
    elif color_code == YELLOW_FOREGROUND:
        print(f"{ESCAPE}{YELLOW_FOREGROUND}", end="")
    elif color_code == BRIGHT_YELLOW_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_YELLOW_FOREGROUND}", end="")
    elif color_code == BLUE_FOREGROUND:
        print(f"{ESCAPE}{BLUE_FOREGROUND}", end="")
    elif color_code == BRIGHT_BLUE_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_BLUE_FOREGROUND}", end="")
    elif color_code == MAGENTA_FOREGROUND:
        print(f"{ESCAPE}{MAGENTA_FOREGROUND}", end="")
    elif color_code == BRIGHT_MAGENTA_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_MAGENTA_FOREGROUND}", end="")
    elif color_code == CYAN_FOREGROUND:
        print(f"{ESCAPE}{CYAN_FOREGROUND}", end="")
    elif color_code == BRIGHT_CYAN_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_CYAN_FOREGROUND}", end="")
    elif color_code == WHITE_FOREGROUND:
        print(f"{ESCAPE}{WHITE_FOREGROUND}", end="")
    elif color_code == BRIGHT_WHITE_FOREGROUND:
        print(f"{ESCAPE}{BRIGHT_WHITE_FOREGROUND}", end="")
    else:
        raise ValueError(
            f"This <{color_code}> Value Doesn't Support By This Function"
        )


def change_background_color(color_code: str) -> None:
    """
        This Function Will Change The Background Color Of The Terminal,
        That Just Support Standard Color.
        All Of Standard Colors Supported By This Function Are:
        {Black, Red, Green, Yellow, Blue, Magenta, Cyan, White
        Bright Black, Bright Red, Bright Green, Bright Yellow,
        Bright Blue, Bright Magenta, Bright Cyan, Bright White}
    """
    if color_code == BLACK_BACKGROUND:
        print(f"{ESCAPE}{BLACK_BACKGROUND}", end="")
    elif color_code == BRIGHT_BLACK_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_BLACK_BACKGROUND}", end="")
    elif color_code == RED_BACKGROUND:
        print(f"{ESCAPE}{RED_BACKGROUND}", end="")
    elif color_code == BRIGHT_RED_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_RED_BACKGROUND}", end="")
    elif color_code == GREEN_BACKGROUND:
        print(f"{ESCAPE}{GREEN_BACKGROUND}", end="")
    elif color_code == BRIGHT_GREEN_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_GREEN_BACKGROUND}", end="")
    elif color_code == YELLOW_BACKGROUND:
        print(f"{ESCAPE}{YELLOW_BACKGROUND}", end="")
    elif color_code == BRIGHT_YELLOW_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_YELLOW_BACKGROUND}", end="")
    elif color_code == BLUE_BACKGROUND:
        print(f"{ESCAPE}{BLUE_BACKGROUND}", end="")
    elif color_code == BRIGHT_BLUE_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_BLUE_BACKGROUND}", end="")
    elif color_code == MAGENTA_BACKGROUND:
        print(f"{ESCAPE}{MAGENTA_BACKGROUND}", end="")
    elif color_code == BRIGHT_MAGENTA_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_MAGENTA_BACKGROUND}", end="")
    elif color_code == CYAN_BACKGROUND:
        print(f"{ESCAPE}{CYAN_BACKGROUND}", end="")
    elif color_code == BRIGHT_CYAN_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_CYAN_BACKGROUND}", end="")
    elif color_code == WHITE_BACKGROUND:
        print(f"{ESCAPE}{WHITE_BACKGROUND}", end="")
    elif color_code == BRIGHT_WHITE_BACKGROUND:
        print(f"{ESCAPE}{BRIGHT_WHITE_BACKGROUND}", end="")
    else:
        raise ValueError(
            f"This <{color_code}> Value Doesn't Support By This Function"
        )


def reset_format() -> None:
    """
        This Function Will Reset All Formats Of The Terminal
    """
    print(f"{ESCAPE}{RESET}", end="")


def set_bold_format() -> None:
    """
        This Function Will Bold The Format Of Available Texts In Terminal
    """
    print(f"{ESCAPE}{SET_BOLD}", end="")


def reset_bold_format() -> None:
    """
        This Function Will UnBold The Format Of Available Texts In Terminal
        Remember This Function Also UnDim The Texts
    """
    print(f"{ESCAPE}{RESET_BOLD}", end="")


def set_dim_format() -> None:
    """
        This Function Will Dim The Format Of Available Texts In Terminal
    """
    print(f"{ESCAPE}{SET_DIM}", end="")


def reset_dim_format() -> None:
    """
        This Function Will UnDim The Format Of Available Texts In Terminal
        Remember This Function Also UnBold The Texts
    """
    print(f"{ESCAPE}{RESET_DIM}", end="")


def set_italic_format() -> None:
    """
        This Function Will Italic The Format Of Available Texts In Terminal
    """
    print(f"{ESCAPE}{SET_ITALIC}", end="")


def reset_italic_format() -> None:
    """
        This Function Will UnItalic The Format Of Available Texts In Terminal
    """
    print(f"{ESCAPE}{RESET_ITALIC}", end="")


def set_under_line_format() -> None:
    """
        This Function Will UnderLine The Format Of Available Texts In
        Terminal
    """
    print(f"{ESCAPE}{SET_UNDER_LINE}", end="")


def reset_under_line_format() -> None:
    """
        This Function Will UnUnderLine The Format Of Available Texts In
        Terminal
    """
    print(f"{ESCAPE}{RESET_UNDER_LINE}", end="")


def set_blink_format() -> None:
    """
        This Function Will Blink The Format Of Available Texts In
        Terminal.
        Remember This Feature May Not Works In Old Terminals.
    """
    print(f"{ESCAPE}{SET_BLINK}", end="")


def reset_blink_format() -> None:
    """
        This Function Will UnBlink The Format Of Available Texts In
        Terminal.
        Remember This Feature May Not Works In Old Terminals.
    """
    print(f"{ESCAPE}{RESET_BLINK}", end="")


def set_reverse_format() -> None:
    """
        This Function Will Reverse The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{SET_REVERSE}", end="")


def reset_reverse_format() -> None:
    """
        This Function Will UnReverse The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{RESET_REVERSE}", end="")


def set_hide_format() -> None:
    """
        This Function Will Hide The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{SET_HIDE}", end="")


def reset_hide_format() -> None:
    """
        This Function Will UnHide The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{RESET_HIDE}", end="")


def set_strike_line_format() -> None:
    """
        This Function Will StrikeLine The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{SET_STRIKE_LINE}", end="")


def reset_strike_line_format() -> None:
    """
        This Function Will UnStrikeLine The Format Of Available Texts In
        Terminal.
    """
    print(f"{ESCAPE}{RESET_STRIKE_LINE}", end="")


def write_colored_text(context: str, foreground_color: str, background_color: str) -> None:
    """
        This Dunction Will Set The Foreground And Background Color Of
        The Terminal Accorded To The Entered Arguments Of This Function
        And Then Write The Context That Entered As First Argument Of
        This Function To The Terminal And Finally Reset All Of The Applied
        Appearance To The Terminal.
    """
    try:
        change_foreground_color(foreground_color)
    except ValueError:
        raise ValueError(
            f"This <{foreground_color}> Doesn't Support By This Function"
        )

    try:
        change_background_color(background_color)
    except ValueError:
        raise ValueError(
            f"This <{background_color}> Doesn't Support By This Function"
        )

    print(context, end="")
    reset_format()


def writeln_colored_text(context: str, foreground_color: str, background_color: str) -> None:
    """
        This Dunction Will Set The Foreground And Background Color Of
        The Terminal Accorded To The Entered Arguments Of This Function
        And Then Write The Context That Entered As First Argument Of
        This Function To The Terminal  And Then Reset All Of The Applied
        Appearance To The Terminal And Finally Move The Cursor To The New Line
        Of The Terminal.
    """
    try:
        change_foreground_color(foreground_color)
    except ValueError:
        raise ValueError(
            f"This <{foreground_color}> Doesn't Support By This Function"
        )

    try:
        change_background_color(background_color)
    except ValueError:
        raise ValueError(
            f"This <{background_color}> Doesn't Support By This Function"
        )

    print(context, end="")
    reset_format()
    print()
