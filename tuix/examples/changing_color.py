from tuix import tuix


def main() -> None:
    # Writes Colored Text In Current Line Of Terminal
    tuix.write_colored_text("This Is Blue With Green Background", tuix.BLUE_FOREGROUND, tuix.GREEN_BACKGROUND)
    # Writes Colored Text In Current Line Of Terminal
    tuix.write_colored_text("This Is Red With Cyan Background", tuix.RED_FOREGROUND, tuix.CYAN_BACKGROUND)
    # Moves The Cursor Of Terminal To The New Line
    print()

    # Writes Colored Text In Current Line Of Terminal And Moves The Cursor To The New Line
    tuix.writeln_colored_text("This Is Blue With Green Background", tuix.BLUE_FOREGROUND, tuix.GREEN_BACKGROUND)
    # Writes Colored Text In Current Line Of Terminal And Moves The Cursor To The New Line
    tuix.writeln_colored_text("This Is Red With Cyan Background", tuix.RED_FOREGROUND, tuix.CYAN_BACKGROUND)


if __name__ == "__main__":
    main()
