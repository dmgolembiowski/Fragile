#!/usr/bin/python3
from __future__ import annotations
#import pudb
#pu.db
from cursesmenu import CursesMenu, SelectionMenu
from cursesmenu import curses_menu as cm
from cursesmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
#from Cursedmenu import CursesMenu, SelectionMenu
#from Cursedmenu import curses_menu as cm
#from Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
import curses
#from .. import core
import os, sys
sys.path.append("/home/david/.local/bin/Fragile/Fragile/")
from pathlib import Path
#from Fragile.core import CreateProject, Main
from core import CreateProject, Main
import random
#import sys
from Mainmenu.helpers import FragileProject, Handler


class BaseMenu:
    def __init__(
            self,
            menu=None,
            cp=None,
            clas=None,
            title="Fragile Project Manager",
            descr="A local goal-planning kanban board inspired by Agile methodologies",
            options=[]):

        self.title = title
        self.descr = descr
        self.items = []

        # Default menu config
        if menu is None:
            self.menu = CursesMenu(title, descr, show_exit_option=False)
        else:
            self.menu = menu
        
        # Default clas(s), app, and cp (..core.CreateProject) config
        if clas is None:
            self.clas = BaseMenu
        else:
            self.clas = clas

        # cp is the bootstrapped NPSApplication
        if cp is None:
            self.cp = CreateProject
        else:
            self.cp = cp

        # A helper object for managing menu <-> app transitions/cleanups
        global handler
        handler = Handler(
                menu=self.menu,
                app=self,
                cp=self.cp,
                clas=self.clas)
        # self.handler = handler

        # options should resemble MenuItem objects,
        # and should probably have __str__ methods defined
        self.options = options

    def savedProjects(self):
        import datetime
        from pathlib import Path
        PATH_TO_RECORDS = str(Path(__file__).parent.absolute()) + '/records.pydict'

        # Get all saved things
        with open(PATH_TO_RECORDS, 'r') as recs:
            _records = recs.read()
        records = eval(_records)
        projects = records['all']

        # Iterate over each and make a FragileProject instance
        for project in projects:
            FragileProject(projects[project]['projectName'], projects[project])
 
    def save(self, item):
        self.menu.append_item(item)
        self.items.append(item)

    def gen_template(self):

        # Opening a saved project
        self.savedProjects()
        opChildMenu = SelectionMenu(FragileProject.each)
        __openProject__ = SubmenuItem(
                "Select a Fragile Project",
                opChildMenu,
                self.menu)
        self.save(__openProject__)

        __createNew__ = FunctionItem(
                "Create a new Fragile Project",
                Main.main,
                args=[handler])
        self.save(__createNew__)

        __memberSpace__ = FunctionItem(
                "Open a Team Member's Fragile Board",
                lambda: None,
                args=[handler])
        self.save(__memberSpace__)

        __lookup__ = MenuItem(
                "Search projects for a file")
        self.save(__lookup__)

        __admin__  = MenuItem(
                "Team Administration")
        self.save(__admin__)

        __dock__   = MenuItem(
                "Configure External Connections")
        self.save(__dock__)

        __dash__   = MenuItem(
                "Dashboard Overview of a Fragile Project")
        self.save(__dash__)

        __cal__    = MenuItem(
                "Calendar of Upcoming Deadlines")
        self.save(__cal__)

        __export__ = MenuItem(
                "Export all project records")
        self.save(__export__)

        __services__ = MenuItem(
                "Manage background Fragile jobs, platforms, services, etc.")
        self.save(__services__)

        __exit__ = FunctionItem(
                "Exit",
                sys.exit)
        self.save(__exit__)
   
    def start_fragile(self):
        def launch(refresh=True):
            if refresh:
                FragileProject.refresh_saved(self.menu.show())
            else:
                self.menu.show()
        cm.clear_terminal()
        launch()

#if __name__ == '__main__':
menu = BaseMenu()
menu.gen_template()
menu.start_fragile()
