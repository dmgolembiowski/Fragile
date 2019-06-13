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
import os
import sys
from ..Cursedmenu import CursesMenu, SelectionMenu
from ..Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
import curses
import json
import IPython
from ..Application import Application
#-----------------------------------------------------------------------------
class Record:
    records = {}
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
class Feature:
    def __init__(self, **kwargs):
        self.feature_title: str
        self.difficulty: float
        self.complete: bool
        self.points: int 
        self.finishDate: str
        self.priority: str
        self.tasks: list
        self.__dict__.update(kwargs)
        for t in range(len(self.tasks)):
            self.tasks[t] = Task(**self.task[t])            

    def write(self) -> dict:
        return self.__dict__

    @staticmethod
    def get():
        template = {}
        return template

class Task:
    def __init__(self, **kwargs):
        self.task_title: str
        self.difficulty: float
        self.complete: bool
        self.points: int
        self.finishDate: str
        self.priority: str
        self.steps: list
        self.__dict__.update(kwargs)
        for s in range(len(self.steps)):
            self.steps[s] = Step(**self.steps[s])

    def write(self) -> dict:
        return self.__dict__

    @staticmethod
    def get():
        template = {}
        return template



class Step:
    def __init__(self, **kwargs):
        self.step_title: str
        self.difficulty: float
        self.complete: bool
        self.points: int
        self.finishDate: str
        self.priority: str
        self.notes: str
        self.__dict__.update(kwargs)
        
    def write(self) -> dict:
        return self.__dict__

    @staticmethod
    def get():
        template = {}
        return template


class Self:
    """ Container for values of FormMultiPageActionWithMenus """
    pass

class CreateProject(npyscreen.NPSApp):
    """ See help(CreateProject.main)"""
    name = "Fragile--Create a new project:"
    npyscreen.disableColor()

    def __init__(self):
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
        npyscreen.disableColor()
        cp = nps.FormMultiPageActionWithMenus(name=CreateProject.name)
        projectName = cp.add(nps.TitleText, name='Project Name:', value='')
        pn = []
        project_description = CreateProject.Textbox(
                form=cp,
                _value_list=pn,
                _name='Description')

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
        
        Priority = {
                0: "High",
                1: "Medium",
                2: "Low"}

        rec = {}
        _all = {}
        names = set()
        rec['all'] = _all
        rec['names'] = names
        rec['names'].add(projectName.value)

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
            'feature_priority': "".join([x for x in fn]),
            'feature_notes': feature_notes.value,
            'tasks': [{
                    'task_title': task_title.value,
                    'task_finishDate': task_finishDate.value,
                    'task_points': task_points.value,
                    'task_priority': Priority[task_priority.value[0]],
                    'task_notes': "".join([x for x in tn]),
                    'steps': [{
                        'step_title': step_title.value,
                        'step_complete': step_complete.value,
                        'step_finishDate': step_finishDate.value,
                        'step_points': step_points.value,
                        'step_priority': Priority[step_priority.value[0]],
                        'step_notes': "".join([x for x in sn])}]
                    }]})

        with open("records.pydict", "w") as f:
            f.write(str(rec))

    def features(self):
        self.feature_title: str
        self.complete: bool
        self.difficulty: float
        self.points = 0
        self.finishDate: str
        self.priority: str
        self.tasks = []
        
    def tasks(self):
        self.task_title: str
        self.complete: bool
        self.difficulty: float
        self.points = 0
        self.finishDate: str
        self.priority: str
        self.steps = []

    def steps(self):
        self.step_title: str
        self.complete: bool
        self.difficulty: float
        self.points = 0
        self.finishDate: str
        self.priority: str
        self.notes = ''
 
    def first_save(self, _features):
        file_path = 'records.json'
        from pathlib import Path
        if Path(f"{file_path}").is_file():
            return self.save(_features)
        with open("template.json", "r") as template:
            records = json.load(template)
        firstProject = {
                'projectName': self.projectName.value,
                'description': self.description.value,
                'startDate': str(self.startDate.value),
                'finishDate': str(self.finishDate.value),
                'features': _features}
        records["names"].append(self.projectName.value)
        records["all"].update({self.projectName.value: firstProject})
        with open("records.json", "w") as savefile:
            json.dump(savefile)
    
    def save(self, _features: list):
        file_path = './records.json'
        this = {
            'projectName': self.projectName.value,
            'description': self.description.value,
            'startDate': str(self.startDate.value),
            'finishDate': str(self.finishDate),
            'features': _features}
        obj = Record(**this)
        with open(file_path, "r") as f:
            Record.records = json.load(f)
        records.append(this)
        for i in range(len(records)):
            cache[records[i]]["projectName"] = records[i]
        with open(file_path, 'w') as f:
            dumping = [cache[key] for key in list(cache)]
            records = json.dumps(dumping, indent=4)
            f.write(records)

'''
@npyscreen.wrapper_basic
def createProject(*args):
    proj = CreateProject()
    proj.run()
'''

class Main:
    @staticmethod
    def create_project(*args):
        proj = CreateProject()
        proj.run()

    @staticmethod
    def main():
        print(npyscreen.wrapper_basic(Main.create_project))
        Application.start_fragile(CreateProject, Main)

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(Main.create_project))
    Application.start_fragile()
