import curses

def main(stdscr):
    curses.curs_set(1)  # Make the cursor visible
    stdscr.addstr("Hello, ")
    stdscr.refresh()  # Refresh the screen to display the text
    name = ""
    stdscr.addstr("What's your name? ")

    while True:
        char = stdscr.getch()  # Get user input one character at a time
        if char == 10:  # Enter key is pressed
            break
        if char == curses.KEY_UP:
            stdscr.addstr("UP")
        name += chr(char)
        stdscr.clear()
        stdscr.addstr(f"Hello, {name}")
        stdscr.addstr(", nice to meet you, ")
        stdscr.addstr(name)  # Display the name as the user types
        stdscr.refresh()

    stdscr.addstr(f", nice to meet you, {name}!\n")
    stdscr.refresh()
    stdscr.getch()  # Wait for another key press to exit

curses.wrapper(main)

