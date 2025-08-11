from tuix import tuix


def main() -> None:
    # Resets All Applied Style From Your Terminal
    tuix.reset_all_format()
    print("This Is Default Style Of Your Terminal")

    # Will Set Style Of Terminal To Bold
    tuix.set_bold_format()
    print("This Is Bold Style Of Your Terminal", end="")
    # Will Reset Style Of Your From Bold Or Dim To Default
    tuix.reset_bold_format()
    print()

    # Will Set Style Of Your Terminal To Dim
    tuix.set_dim_format()
    print("This Is Dim Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Dim Or Bold To Default
    tuix.reset_dim_format()
    print()

    # Will Set Style Of Your Terminal To Italic
    tuix.set_italic_format()
    print("This Is Italic Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Italic To Default
    tuix.reset_italic_format()
    print()

    # Will Set Style Of Your Terminal To Under Line
    tuix.set_under_line_format()
    print("This Is Under Line Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Under Line To Default
    tuix.reset_under_line_format()
    print()

    # Will Set Style Of Your Terminal To Blink
    tuix.set_blink_format()
    print("This Is Blink Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Blink To Default
    tuix.reset_blink_format()
    print()

    # Will Set Style Of Your Terminal To Reverse
    tuix.set_reverse_format()
    print("This Is Reverse Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Reverse To Default
    tuix.reset_reverse_format()
    print()

    # Will Set Style Of Your Terminal To Hide
    tuix.set_hide_format()
    print("This Is Hide Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Hide To Default
    tuix.reset_hide_format()
    print()

    # Will Set Style Of Your Terminal To Strike Line
    tuix.set_strike_line_format()
    print("This Is Strike Line Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Strike Line To Default
    tuix.reset_strike_line_format()
    print()

    # Will Set Style Of Your Terminal To Bold
    tuix.set_format(tuix.SET_BOLD)
    # Will Set Style Of Your Terminal To Italic
    tuix.set_format(tuix.SET_ITALIC)
    print("These Are Bold And Italic Styles Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Italic
    tuix.reset_format(tuix.RESET_ITALIC)
    print()
    print("This Is Bold Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Bold
    tuix.reset_format(tuix.RESET_BOLD)
    print()

    # Will Set Style Of Your Terminal To Bold And Italic And Under Line
    tuix.set_formats([tuix.SET_BOLD, tuix.SET_ITALIC, tuix.SET_UNDER_LINE])
    print("These Are Bold And Italic And Under Line Styles Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Bold And Italic
    tuix.reset_formats([tuix.RESET_BOLD, tuix.RESET_ITALIC])
    print()
    print("This Is Under Line Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Under Line
    tuix.reset_format(tuix.RESET_UNDER_LINE)
    print()


if __name__ == "__main__":
    main()
