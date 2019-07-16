"""
Fragile.core: Terminal application for managing and tracking projects in production.
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
from __future__ import annotations
import npyscreen
nps = npyscreen
import threading
import os
import sys
#from ..Cursedmenu import CursesMenu, SelectionMenu, curses_menu
#from ..Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
#from .Extensions import FileExplorer
import curses
import json
import IPython
import subprocess
import functools
import datetime
from pathlib import Path
class Self:
    """ Container for values of FormMultiPageActionWithMenus """
    pass

class CreateProject(npyscreen.NPSAppManaged):
    """ See help(CreateProject.main)"""
    name = "Fragile--Create a new project:"
    handler = None
    #npyscreen.disableColor()

    def __init__(self):
        self.handler = CreateProject.handler
        self = Self

    @staticmethod
    def Textbox(
            form,
            _value_list,
            _name='Text Box',
            _max_height=6,
            _footer="Press [i|o] to insert values",
            _slow_scroll=False):
        return form.add(npyscreen.MultiLineEditableBoxed,
                max_height=_max_height,
                name=_name,
                footer=_footer,
                values=_value_list,
                slow_scroll=_slow_scroll)

    def main(self):
        """ CreateProject.main() overloads npyscreen.NPSApp.main()
        The real action comes from the class
        `npyscreen.FormMultiPageActionWithMenus`, which comes from
        /path/to/npyscreen/fmFormMultiPage.py

        cp = nps.FormMultiPageActionWithMenus(name="Fragile: Create a new project:")
        """
        cp = nps.FormMultiPageActionWithMenus(name=CreateProject.name)
        projectName = cp.add(nps.TitleText, name='Project Name:', value='')
        pn = []
        project_description = CreateProject.Textbox(
                form=cp,
                _value_list=pn,
                _name='Description')
        project_location = cp.add(nps.TitleFilenameCombo, name='Repository Location')
        #cp.add_widget_intelligent(nps.FileSelector, message=nps.selectFile('~/'))
        # Maybe add the box for choosing project directory/Git Repo
        startDate = cp.add(nps.TitleDateCombo, name='Start Date:')
        finishDate = cp.add(nps.TitleDateCombo, name='Finish Date:')
        num_features = cp.add(
                nps.TitleSlider,
                out_of=20,
                name='No. Features:')
         
        # Create One "Features" Page
        cp.switch_page(0)
        #features = []
        feature_page = cp.add_page()
        feature_title = cp.add(
                nps.TitleText,
                name="Feature Label:",
                value='')
        
        feature_difficulty = cp.add(
                nps.TitleSlider,
                out_of=11,
                name="Difficulty:",
                value=0.0)
        
        feature_finishDate = cp.add(
                nps.TitleDateCombo, name="Finish Date:")
 
        feature_points = cp.add(
                nps.TitleSlider,
                name="Effort Points:",
                out_of=64.0)
        feature_location = cp.add(
                nps.TitleFilenameCombo,
                name='Feature')
        feature_priority = cp.add(
                npyscreen.TitleSelectOne,
                max_height=4,
                value=[0,],
                name="Indicate the Priority:",
                values=["High","Medium","Low"],
                scroll_exit=True)
        fn = []
        feature_notes = CreateProject.Textbox(
                form=cp,
                _value_list=fn,
                _name='(Optional Notes)')

        cp.switch_page(1)

        # Create One "Tasks" Page
        tasks_page = cp.add_page()
        task_title = cp.add(
                nps.TitleText,
                name="Task Label: ",
                value='')

        task_finishDate = cp.add(
                nps.TitleDateCombo, name="Finish Date:")

        task_points = cp.add(
                nps.TitleSlider,
                out_of=64,
                name="Points",
                value=0.0)

        task_priority = cp.add(
                npyscreen.TitleSelectOne,
                max_height=5,
                value=[0,],
                name="Indicate the Priority:",
                values=["High","Medium","Low"])
        tn = []
        task_notes = CreateProject.Textbox(
                form=cp,
                _value_list=tn,
                _name='(Optional Notes)')

        cp.switch_page(2)
        

        # Create One "Steps" Page
        step_page = cp.add_page()
        step_title = cp.add(
                nps.TitleText,
                name="Step Label: ",
                value='')
        
        step_complete = cp.add(
                nps.TitleSelectOne,
                max_height=4,
                name="Step Completed:",
                values=["True", "False"],
                value=[1,])

        step_finishDate = cp.add(
                nps.TitleDateCombo, name="Finish Date:")

        step_points = cp.add(
                nps.TitleSlider,
                out_of=32,
                name="Points:",
                value=0.0)
        
        step_priority = cp.add(
                npyscreen.TitleSelectOne,
                max_height=5,
                value=[0,],
                name="Indicate the Priority:",
                values=["High","Medium","Low"])

        sn = []
        step_notes = CreateProject.Textbox(
                form=cp,
                _value_list = sn,
                _max_height=10,
                _name='(Optional Notes)')

        cp.switch_page(3)

        on_ok = lambda: npyscreen.notify_confirm("Project saved!")
        cp.on_ok = on_ok
        cp.edit()
        ''' For future me to use        
        Priority = {
                0: "High",
                1: "Medium",
                2: "Low"}
        '''
        # Bring up everything saved from previous sessions
        records_pydict = Path(__file__).parent.absolute()
        records_pydict = str(records_pydict)
        records_pydict += "/records.pydict"
        with open(records_pydict, "r") as f:
            saved = f.read()
        saved = eval(saved)
        
        # Creating newest record instance
        rec = {}
        _all = {}
        names = set()
        rec['all'] = _all
        rec['names'] = names
        rec['names'].add(projectName.value)

        # Filling in ALL of the attributes
        rec['all'].update({projectName.value: {
            'projectName': projectName.value,
            'project_description': pn,
            'startDate': startDate.value,
            'finishDate': finishDate.value,
            'features': {}}})

        rec['all'][projectName.value]['features'].update({
            'feature_title': feature_title.value,
            'feature_difficulty': feature_difficulty.value,
            'feature_finishDate': feature_finishDate.value,
            'feature_points': feature_points.value,
            'feature_priority': feature_priority.value,
            'feature_notes': fn,
            'tasks': [{
                    'task_title': task_title.value,
                    'task_finishDate': task_finishDate.value,
                    'task_points': task_points.value,
                    'task_priority': task_priority.value,
                    'task_notes': tn,
                    'steps': [{
                        'step_title': step_title.value,
                        'step_complete': step_complete.value,
                        'step_finishDate': step_finishDate.value,
                        'step_points': step_points.value,
                        'step_priority': step_priority.value,
                        'step_notes': step_notes.value}]
                    }]})

        # Now, we merge the two records into one container
        saved['names'] = saved['names'].union(rec['names'])
        saved['all'].update(rec['all'])
        
        with open(records_pydict, "w") as f:
            f.write(str(saved))

        # Call core.Main.resume(handler=CreateProject.handler)
        Main.resume(self.handler)

def call_counter(function):
    create_project_count = 0
    main_count = 0
    resume_count = 0

    @functools.wraps(function)
    def result(*args, **kwargs):
        nonlocal create_project_count
        nonlocal main_count
        nonlocal resume_count
        if function.__name__ == 'create_project':
            create_project_count += 1
            Main.create_project_count = create_project_count
        elif function.__name__ == 'main':
            main_count += 1
            Main.main_count = main_count
        elif function.__name__ == 'resume_count':
            resume_count += 1
            Main.resume_count = resume_count
        return function(*args, **kwargs)
    return result

class Main:
    create_project_count = 0
    main_count = 0
    resume_count = 0

    @staticmethod
    @call_counter
    def create_project(*args):
        proj = CreateProject()
        proj.run()

    @staticmethod
    @call_counter
    def main():
        #CreateProject.handler = handler
        #handler.clear_screen()
        #handler.menu_pause()
        print(npyscreen.wrapper_basic(Main.create_project))

    @staticmethod
    @call_counter
    def resume():
        #handler.menu.draw()
        #handler.menu_resume()
        #sys.exit(handler.app.start_fragile(doUpdate=True))
        nps.blank_terminal()
        curses.echo()
        curses.curs_set(1)
        curses.nocbreak()
        curses.endwin()
        sys.exit(handler.clas._start_fragile())

if __name__ == '__main__':
    Main.main()
