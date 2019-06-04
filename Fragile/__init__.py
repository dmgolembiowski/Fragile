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
from .Cursedmenu.items import SubmenuItem, CommandItem, MenuItem

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

class Application:
    @staticmethod
    def start_fragile():
        description = 'A local goal-planning kanban board inspired by Agile methodologies.'
        menu = CursesMenu('Fragile Project Manager', description)

        def launch():
            nonlocal description
            nonlocal menu

            ''' 1 - Open/Edit a project '''
            # Replace `openProject`'s options
            openProject = SelectionMenu(
                    ["item1", "item2", "item3"]
                )
            __openProject__ = SubmenuItem(
                    "Open an existing project", 
                    openProject, 
                    menu) 

            ''' 2 - Create a new project '''
            createNew = SelectionMenu(
                    ["Need form here"]
                )
            __createNew__ = SubmenuItem(
                    "Create a new project",
                    createNew,
                    menu)

            ''' 3 - Search your projects '''
            __search__ = MenuItem("Search for comments")

            for item in [__openProject__, __createNew__, __search__]:
                menu.append_item(item)
            menu.show()

        launch()

if __name__ == '__main__':
    Application.start_fragile()
