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
sys.path.append(os.path.join(os.path.dirname(__file__), "extensions"))
from .Cursedmenu import CursesMenu, SelectionMenu
from .Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
import curses
import json
import IPython
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
    def __init__(self):
        self = Self

    def main(self):
        """ CreateProject.main() overloads npyscreen.NPSApp.main()
        The real action comes from the class
        `npyscreen.FormMultiPageActionWithMenus`, which comes from
        /path/to/npyscreen/fmFormMultiPage.py

        cp = nps.FormMultiPageActionWithMenus(name="Fragile: Create a new project:")
       """
        cp = nps.FormMultiPageActionWithMenus(name=CreateProject.name)
        projectName = cp.add(nps.TitleText, name='Project Name:')
        description  = cp.add(nps.TitleText, name='Description:')
        startDate = cp.add(nps.TitleDateCombo, name='Start Date:')
        finishDate = cp.add(nps.TitleDateCombo, name='Finish Date:')
        #_num = cp.add(
        #         nps.TitleSlider,
        #         out_of=20,
        #         name='Est. No. of High-Level Features:')
        
        # Create One "Features" Page
        cp.switch_page(0)
        features = []
        feature_page = cp.add_page()
        feature_title = cp.add(
                nps.TitleText,
                name="Feature Label:")
        
        #feature_complete = cp.add(
        #        nps.TitleSelectOne,
        #        max_height=4,
        #        name="Feature Completed?",
        #        values=["True", "False"],
        #        value=[1,])
        
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
        cp.switch_page(1)
        tasks = []

        # Create One "Tasks" Page
        tasks_page = cp.add_page()
        task_title = cp.add(
                nps.TitleText,
                name="Task Label: ")

        #tasks_complete = cp.add(
        #        nps.TitleSelectOne,
        #        max_height=4,
        #        name="Task Completed?",
        #        values=["True", "False"],
        #        value=[1,])

        tasks_finishDate = cp.add(
                nps.TitleDateCombo, name="Finish Date:")

        tasks_points = cp.add(
                nps.TitleSlider,
                out_of=11,
                name="Points",
                value=0.0)

        tasks_priority = cp.add(
                npyscreen.TitleSelectOne,
                max_height=5,
                value=[0,],
                name="Indicate the Priority:",
                values=["High","Medium","Low"])

        tasks_notes = cp.add(
                npyscreen.BoxTitle,
                max_height=9,
                name="Notes: (Highlight and press Enter to edit)",
                scroll_exit=True)
        cp.switch_page(2)
        
        steps = []

        # Create One "Steps" Page
        steps_page = cp.add_page()
        steps_title = cp.add(
                nps.TitleText,
                name="Step: ")
        
        steps_complete = cp.add(
                nps.TitleSelectOne,
                max_height=4,
                name="Step Completed:",
                values=["True", "False"],
                value=[1,])

        steps_finishDate = cp.add(
                nps.TitleDateCombo, name="Finish Date:")

        steps_points = cp.add(
                nps.TitleSlider,
                out_of=32,
                name="Points:",
                value=0.0)
        
        steps_priority = cp.add(
                npyscreen.TitleSelectOne,
                max_height=5,
                value=[0,],
                name="Indicate the Priority:",
                values=["High","Medium","Low"])
        
        steps_notes = cp.add(
                npyscreen.BoxTitle,
                max_height=9,
                name="Notes: (Highlight and press Enter to edit)")
         
        cp.switch_page(3)

        on_ok = lambda: npyscreen.notify_confirm("Project saved!")
        cp.on_ok = on_ok
        cp.edit()

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
        file_path = 'records.json'
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
def createProject():
    proj = CreateProject()
    proj.run()
'''
def main_project(*args):
    proj = CreateProject()
    proj.run()

def main():
    print(npyscreen.wrapper_basic(main_project))

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(main_project))
