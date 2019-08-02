from __future__ import annotations
import curses
import time

# Curses does allow non-blocking key-input as well

@curses.wrapper
def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    width = 4
    count = 0
    direction = 1
    np = curses.newpad(24, 80)
    while True:
        c = stdscr.getch()

        # Top Row Part
        stdscr.addch(1, 1, curses.ACS_HLINE)
        stdscr.addch(1, 2, curses.ACS_TTEE) # Connect down @(2,2)
        stdscr.addch(1, 3, curses.ACS_HLINE)
        stdscr.addstr(1, 5, "{{ r['all'][projectName] }}")

        # Depth 2
        stdscr.addch(2, 2, curses.ACS_VLINE)
        stdscr.addch(3,2, curses.ACS_LTEE)
        stdscr.addch(4,2, curses.ACS_VLINE)
        stdscr.addch(5,2, curses.ACS_VLINE)
        stdscr.addch(6,2, curses.ACS_VLINE)
        stdscr.addch(7,2, curses.ACS_VLINE)
        stdscr.addch(8,2, curses.ACS_VLINE)
        stdscr.addch(9,2, curses.ACS_VLINE)
        stdscr.addch(10,2, curses.ACS_VLINE)
        stdscr.addch(11,2, curses.ACS_VLINE)
        stdscr.addch(12,2, curses.ACS_VLINE)
        stdscr.addch(13,2, curses.ACS_VLINE)
        stdscr.addch(14,2, curses.ACS_VLINE)
        stdscr.addch(15,2, curses.ACS_VLINE)
        stdscr.addch(16,2, curses.ACS_VLINE)
        stdscr.addch(17,2, curses.ACS_LLCORNER)
        stdscr.addstr(17,4, "+ Add a New Feature")


        # Depth 3
        stdscr.addch(3, 3, curses.ACS_HLINE)
        stdscr.addch(3, 4, curses.ACS_HLINE)
        stdscr.addch(3, 5, curses.ACS_HLINE)
        stdscr.addch(3, 6, curses.ACS_HLINE)
        stdscr.addch(3,7, curses.ACS_TTEE)
        stdscr.addch(3, 8, curses.ACS_HLINE)
        stdscr.addstr(3, 10, "{{ r['all'][projectName]['features'][0]['featureName'] }}")
        """stdscr.addch(4, 4, curses.ACS_VLINE)
        stdscr.addch(5, 4, curses.ACS_VLINE)
        stdscr.addch(6, 4, curses.ACS_VLINE)
        stdscr.addch(7,4 , curses.ACS_VLINE)
        stdscr.addch(8,4, curses.ACS_VLINE)
        stdscr.addch(9,4, curses.ACS_VLINE)
        stdscr.addch(10,4, curses.ACS_VLINE)
        stdscr.addch(11,4, curses.ACS_VLINE)
        stdscr.addch(12,4, curses.ACS_VLINE)
        stdscr.addch(13,4, curses.ACS_VLINE)
        stdscr.addch(14,4, curses.ACS_VLINE)
        stdscr.addch(15, 4, curses.ACS_LLCORNER)
        stdscr.addstr(15, 6, "+ Add a New Task")
        """

        # Depth 4
        stdscr.addch(4,7, curses.ACS_VLINE)
        stdscr.addch(5,7, curses.ACS_LTEE)
        stdscr.addch(6, 7, curses.ACS_VLINE)
        stdscr.addch(7,7 , curses.ACS_VLINE)
        stdscr.addch(8,7, curses.ACS_VLINE)
        stdscr.addch(9,7, curses.ACS_VLINE)
        stdscr.addch(10,7, curses.ACS_VLINE)
        stdscr.addch(11,7, curses.ACS_VLINE)
        stdscr.addch(12,7, curses.ACS_VLINE)
        stdscr.addch(13,7, curses.ACS_VLINE)
        stdscr.addch(14,7, curses.ACS_VLINE)
        stdscr.addch(15,7, curses.ACS_LLCORNER)
        stdscr.addstr(15, 9, "+ Add a New Task")


        # Depth 5
        stdscr.addch(5,8, curses.ACS_HLINE)
        stdscr.addch(5, 9, curses.ACS_HLINE)
        stdscr.addch(5, 10, curses.ACS_HLINE)
        stdscr.addch(5, 11, curses.ACS_TTEE) # Begin third vertical line
        stdscr.addch(5, 12, curses.ACS_HLINE)
        #stdscr.addch(5, 13, curses.ACS_HLINE) <- visual space
        stdscr.addstr(5, 14, "{{ r['all'][projectName]...['tasks'][0] }}")

        stdscr.addch(6, 11, curses.ACS_VLINE)
        stdscr.addch(7, 11, curses.ACS_LTEE) # Begin nesting all steps + Step Generator
        stdscr.addch(8, 11, curses.ACS_VLINE)
        stdscr.addch(9, 11, curses.ACS_VLINE)
        stdscr.addch(10, 11, curses.ACS_VLINE)
        stdscr.addch(11, 11, curses.ACS_VLINE)
        stdscr.addch(12, 11, curses.ACS_VLINE)
        stdscr.addch(13, 11, curses.ACS_LLCORNER)
        stdscr.addstr(13, 13, "+ Add a New Step")
        
        # Depth 6
        stdscr.addch(7, 13, curses.ACS_HLINE)
        stdscr.addstr(7, 13, "{{ r['all'][projectName]...['steps'][0]['stepName'] }}")
        stdscr.addch(7, 13, curses.ACS_LTEE)
        #stdscr.addstr(9, 13, "{{ r['all][projectName]...['steps'][1]['stepName'] }}")
        #stdscr.addch(, 15, curses.ACS_LTEE)


        """
        with open("codes.txt", "w+") as f:
            f.write(f"curses.ACS_VLINE={curses.ACS_VLINE}\ncurses.ACS_HLINE={curses.ACS_HLINE}\ncurses.TTEE={curses.ACS_TTEE}\ncurses.ACS_LLCORNER={curses.ACS_LLCORNER}")
        # Clear out anything else the user has typed in
        curses.flushinp()
        #stdscr.clear()
        """
        '''
        # If the user presses p, increase the width of the springy bar
        if c == ord('p'):
            width += 1
        # Draw a springy bar
        stdscr.addstr("#" * count)
        count += direction
        if count == width:
            direction = -1
        elif count == 0:
            direction = 1
        '''
        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)

main()
"""
Calling stdscr.nodelay(True) made stdscr.getch() non-blocking. If Python gets to
that line and the user hasn't typed anything since last time, getch will return
-1, which doesn't match any key.

What if the user managed to type more than one character since the last time
getch was called? All of those characters will start to build up, and getch will
return the value for each one in the order that they came. This can cause
delayed reactions if you're writing a game. After getch, you can call
curses.flushinp to clear out the rest of the characters that the user typed.

This is a good place to talk more about getch.

Every time the user presses a key, that key's value gets stored in a list. When
getch is called, it goes to that list and pops that value. If the user manages
to press several keys before getch is called, getch will pop the least recently
added value (the oldest key pressed). The rest of the keys remain in the list!
The process continues like this. So there's a problem if there is a delay
between calls to getch: Key values can build up. If you don't want this to
happen, curses.flushinp() clears the list of inputted values. This ensures that
the next key the user presses after curses.flushinp() is what getch will return
next time it is called.
"""

"""
To continue learning about curses, checkout the addstr method to see how you can
print strings at certain y, x coordinates. You can start here:
https://docs.python.org/3/library/curses.html#window-objects
"""
