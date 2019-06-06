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
    """ See help(CreateProject.main)
    
    """
    def __init__(self):
        self = Self

    def main(self, target='project_page'):
        """ CreateProject.main() overloads npyscreen.NPSApp.main()
        The real action comes from the class
        `npyscreen.FormMultiPageActionWithMenus`, which comes from
        /path/to/npyscreen/fmFormMultiPage.py

        cp = nps.FormMultiPageActionWithMenus(name="Fragile: Create a new project:")
        _projectName = cp.add(nps.TitleText, name='Project Name:')
        _description  = cp.add(nps.TitleText, name='Description:')
        _startDate = cp.add(nps.TitleDateCombo, name='Select today\'s Date:')
        _finishDate = cp.add(nps.TitleDateCombo, name='Deadline:')
        #_numFeatures = cp.add(nps.TitleText, name='No. of Features:', value=1)
        _numFeatures = Self
        _numFeatures.value = 1
        """
        nonlocal _features = {}
        def project_page():
             cp = nps.FormMultiPageActionWithMenus(name="Fragile--Create a new project:")
            _projectName = cp.add(nps.TitleText, name='Project Name:')
            _description  = cp.add(nps.TitleText, name='Description:')
            _startDate = cp.add(nps.TitleDateCombo, name='Start Date:')
            _finishDate = cp.add(nps.TitleDateCombo, name='Finish Date:')
            _numFeatures = cp.add(nps.TitleSlider, out_of=20, name='Est. No. of High-Level Features:')
                

        def feature_pages(num_features):
            pass
        
        def task_pages(num_tasks):
            pass

        def step_pages(num_pages):
            pass

       
        feature_page = cp.add_page()
 
    def features(self):
        self.feature_title = self.erase
        self.difficulty =
        self.complete = 
        self.points = 
        self.finishDate =
        self.priority = 
        self.tasks =
        
    def tasks(self):

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

def createProject(*args):
    proj = NewProject(name="Creating a new project: ")
    proj.edit()
    #proj.save()

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(createProject))
