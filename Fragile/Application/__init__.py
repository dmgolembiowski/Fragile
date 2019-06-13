#!/usr/bin/python3.7
from ..Cursedmenu import CursesMenu, SelectionMenu
from ..Cursedmenu.items import SubmenuItem, MenuItem, FunctionItem
#from ..Core import CreateProject, Main


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
    #from ..Core import Main
    @staticmethod
    def start_fragile(CreateProject=None, Main=None):
        description = 'A local goal-planning kanban board inspired by Agile methodologies.'
        __menu__ = CursesMenu('Fragile Project Manager', description)
        if CreateProject and Main:
            class Self:
                pass
            class Core:
                def __init__(self):
                    self = Self
            core = Core()
            core.main = Main
            core.CreateProject = CreateProject

        def launch():
            nonlocal description
            nonlocal __menu__

            ''' 1 - Open/Edit a project '''
            # Replace `openProject`'s options
            openProject = SelectionMenu(
                    ["item1", "item2", "item3"]
                )
            __openProject__ = SubmenuItem(
                    "Open or Modify a Project", 
                    openProject, 
                    __menu__) 

            ''' 2 - Create a new project '''
            __createNew__ = FunctionItem(
                    "Create a new project",
                    core.main)

            ''' 3 - Search for a project or file '''
            __search__ = MenuItem("Search for a project or file")

            for item in [__openProject__, __createNew__, __search__]:
                __menu__.append_item(item)
            __menu__.show()

        launch()
