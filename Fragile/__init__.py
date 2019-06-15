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
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "extensions"))
import socket
from .Cursedmenu import CursesMenu, SelectionMenu
from .Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
#from .Application import Application
import curses
#from .Core import CreateProject, Main
from .core import CreateProject, Main
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
    def __init__(self, menu, app, cp):
        """
        Handler.menu -> instance of Cursedmenu.CursesMenu
        Handler.app  -> instance of Fragile.Application
        Handler.cp   -> instance of core.CreateProject
        """
        
        self.menu = menu
        self.app = app
        self.cp = cp

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

class Application:
    def __init__(self):
        pass
    def memetest(self):
        pass

    def start_fragile(self): 
        descr = 'A local goal-planning kanban board inspired by Agile methodologies.'
        menu = CursesMenu('Fragile Project Manager', descr)
        handler = Handler(menu=menu, app=self, cp=CreateProject)

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

            for item in [__openProject__, __createNew__, __search__]:
                menu.append_item(item)
            menu.show()

        launch()
