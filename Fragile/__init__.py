# encoding: utf-8
"""
Fragile: Terminal application for managing and tracking projects in production.
"""
#
#-----------------------------------------------------------------------------
#  Copyright (c) 2019, David Golembiowski <dmgolembiowski@gmail.com>
#
#  Distributed under the terms of the Apache License 2.0
#
#  The full license is in the file LICENSE of this repository.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports 
#-----------------------------------------------------------------------------
import threading
import time
import sys
import os
import socket
from .Cursedmenu import CursesMenu, SelectionMenu, curses_menu
from .Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
import curses
from .core import CreateProject, Main
import functools

def print_debugger(function):
    @functools.wraps(function)
    def result(*args, **kwargs):
        debugName = function.__name__ + "("
        if args:
            for i, arg in enumerate(args):
                if i != 0:
                    debugName += ", "
                debugName += repr(arg)
        if kwargs:
            for i, (arg, val) in enumerate(kwargs.items()):
                if i != 0 or len(args) > 0:
                    debugName += ", "
                debugName += str(arg) + "=" + str(val)
        debugName += ")"
        print(f"C {debugName}")
        res = function(*args, **kwargs)
        if res:
            print(f"R {debugName} = {res}")
        return res
    return result
#-----------------------------------------------------------------------------

class User:
    try:
        name = os.environ['HOME'].strip('/home/')
    except Exception:
        name = 'user'
    try:
        hname = socket.gethostname()
    except Exception:
        hname = 'fragile $ '
    termtag = name + '@' + hname


class Handler:
    def __init__(self, menu, app, cp, clas):
        """
        Handler.menu -> instance of Cursedmenu.CursesMenu
        Handler.app  -> instance of Fragile.Application
        Handler.cp   -> instance of core.CreateProject
        """
        
        self.menu = menu
        self.app = app
        self.cp = cp
        self.clas = clas

    def menu_start(self):
        self.menu.start()

    def menu_exit(self):
        self.menu.exit()

    def menu_join(self):
        self.menu.join()

    def menu_draw(self):
        self.menu.draw()

    def menu_pause(self):
        self.menu.pause()

    def menu_resume(self):
        self.menu.resume()

    def await_start(self, timeout=1):
        self.menu.wait_for_start(timeout)

    def clear_screen(self):
        self.menu.clear_screen()

    def wrap_start(self):
        self.menu.should_exit = True
        for t in threading.enumerate():
            if t is self.menu._main_thread:
                continue
            t.join()
        """
        #self.menu._main_thread.join()
        ## but currently_active_menu probably == None
        CursesMenu.currently_active_menu = None
        # ah, great, we'll just enforce it
        self.menu.should_exit = False
        try:
            self.menu.remove_exit()
        except Exception:
            pass
        try:
            self.menu._main_thread = threading.Thread(
                    target=self.menu._wrap_start,
                    daemon=True)
        except TypeError:
            self.menu._main_thread = threading.Thread(
                    target=self._wrap_start)
            self.menu._main_thread.daemon = True
        self.menu._main.daemon = True
        self.menu._main_thread.start()
        self.menu._main_thread.join(timeout=None)
        if self.menu.parent is None:
            curses.wrapper(self.menu._main_loop)
        else:
            self.menu._main_loop(None)
        CursesMenu.currently_active_menu = None
        self.menu.clear_screen()
        curses_menu.clear_terminal()
        CursesMenu.currently_active_menu = self.menu.previous_active_menu
        """
        self.menu.clear_screen()
        curses_menu.clear_terminal()

class Application:
    def __init__(self):
        pass

    def start_fragile(self):
        curses_menu.clear_terminal()
        descr = 'A local goal-planning kanban board inspired by Agile methodologies.'
        menu = CursesMenu('Fragile Project Manager', descr, show_exit_option=False)
        handler = Handler(menu=menu, app=self, cp=CreateProject, clas=Application)

        def launch():
            nonlocal descr
            nonlocal menu
            nonlocal handler

            ''' 1 - Open/Edit a project '''
            # Replace `openProject`'s options
            openProject = SelectionMenu(
                    ["item1", "item2", "item3"]
                )
            __openProject__ = SubmenuItem(
                    "Open or Modify a Project", 
                    openProject, 
                    menu) 

            ''' 2 - Create a new project '''
            __createNew__ = FunctionItem(
                    "Create a new project",
                    Main.main,
                    args=[handler])

            ''' 3 - Search for a project or file '''
            __search__ = MenuItem("Search for a project or file")

            __exit__ = FunctionItem(
                    "Exit",
                    sys.exit)

            for item in [
                    __openProject__,
                    __createNew__,
                    __search__,
                    __exit__]:
                menu.append_item(item)
            menu.show()
        launch()

    @staticmethod
    def _start_fragile():
        # A sleazy way to reconnect with the main menu and redraw
        _app = Application()
        sys.exit(_app.start_fragile())

