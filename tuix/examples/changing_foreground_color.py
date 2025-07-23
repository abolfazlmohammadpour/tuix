from tuix import tuix


def main() -> None:
    print("This Is Default Foreground Color Of Your Terminal")

    # Changing The Foreground Color To Black
    tuix.change_foreground_color(tuix.BLACK_FOREGROUND)
    print("This Is Black Foreground Color")

    # Changing The Foreground Color To Bright Black
    tuix.change_foreground_color(tuix.BRIGHT_BLACK_FOREGROUND)
    print("This Is Bright Black Foreground Color")

    # Changing The Foreground Color To Red
    tuix.change_foreground_color(tuix.RED_FOREGROUND)
    print("This Is Red Foreground Color")

    # Changing The Foreground Color To Bright Red
    tuix.change_foreground_color(tuix.BRIGHT_RED_FOREGROUND)
    print("This Is Bright Red Foreground Color")

    # Changing The Foreground Color To Green
    tuix.change_foreground_color(tuix.GREEN_FOREGROUND)
    print("This Is Green Foreground Color")

    # Changing The Foreground Color To Bright Green
    tuix.change_foreground_color(tuix.BRIGHT_GREEN_FOREGROUND)
    print("This Is Bright Green Foreground Color")

    # Changing The Foreground Color To Yellow
    tuix.change_foreground_color(tuix.YELLOW_FOREGROUND)
    print("This Is Yellow Foreground Color")

    # Changing The Foreground Color To Bright Yellow
    tuix.change_foreground_color(tuix.BRIGHT_YELLOW_FOREGROUND)
    print("This Is Bright Yellow Foreground Color")

    # Changing The Foreground Color To Blue
    tuix.change_foreground_color(tuix.BLUE_FOREGROUND)
    print("This Is Blue Foreground Color")

    # Changing The Foreground Color To Bright Blue
    tuix.change_foreground_color(tuix.BRIGHT_BLUE_FOREGROUND)
    print("This Is Bright Blue Foreground Color")

    # Changing The Foreground Color To Magenta
    tuix.change_foreground_color(tuix.MAGENTA_FOREGROUND)
    print("This Is Magenta Foreground Color")

    # Changing The Foreground Color To Bright Magenta
    tuix.change_foreground_color(tuix.BRIGHT_MAGENTA_FOREGROUND)
    print("This Is Bright Magenta Foreground Color")

    # Changing The Foreground Color To Cyan
    tuix.change_foreground_color(tuix.CYAN_FOREGROUND)
    print("This Is Cyan Foreground Color")

    # Changing The Foreground Color To Bright Cyan
    tuix.change_foreground_color(tuix.BRIGHT_CYAN_FOREGROUND)
    print("This Is Bright Cyan Foreground Color")

    # Changing The Foreground Color To White
    tuix.change_foreground_color(tuix.WHITE_FOREGROUND)
    print("This Is White Foreground Color")

    # Changing The Foreground Color To Bright White
    tuix.change_foreground_color(tuix.BRIGHT_WHITE_FOREGROUND)
    print("This Is Bright White Foreground Color")

    # Reset All Of The Appearance Themes
    tuix.reset_all_format()


if __name__ == "__main__":
    main()
