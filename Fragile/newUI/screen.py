#!/usr/bin/python3
import curses
import time
import IPython

def dimensions(stdscr):
    y, x = stdscr.getmaxyx()
    return y, x

@curses.wrapper
def window(stdscr, returnScreen=True, noDelay=True, pipe=lambda stdscr: IPython.embed()):
    stdscr.nodelay(noDelay)
    stdscr.clear()
    if pipe is not None:
        while True:
            try:
                if returnScreen:
                    pipe(stdscr)
                else:
                    pipe()
            finally:
                curses.endwin()
    else:
        curses.endwin()

window()
