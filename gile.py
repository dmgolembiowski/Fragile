#!/usr/bin/python3m
from cursesmenu import *
from cursesmenu.items import *
import sys
import socket
import os


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

def main_menu():
    description = 'A local goal-planning kanban board inspired by Agile methodologies.'
    menu = CursesMenu('Fragile Project Manager', description)
    
    ''' 1 - Open/Edit a project '''
    # Replace `openProject`'s options
    openProject = SelectionMenu(["item1", "item2", "item3"])
    __openProject__ = SubmenuItem("Open a project", openProject, menu) 

    ''' 2 - Create a new project '''
    createNew = SelectionMenu(["Need form here"])
    __createNew__ = SubmenuItem("Create a new project", createNew, menu)

    ''' 3 - Search your projects '''
    #__terminal__ = CommandItem("Run a terminal command", "ls")
    __search__ = MenuItem("Search your projects")

    for item in [__openProject__, __createNew__, __search__]:
        menu.append_item(item)

    menu.show()

main_menu()
    
"""
# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
"""
