#!/usr/bin/env python
from __future__ import annotations
import npyscreen as nps
import random

RETURN = []

class FragileTree(nps.npysTree.TreeData):
    _ID = {}

    def __init__(self, refresh_Branch_ID=True, **kwargs):
        self._id = hash(random.random())
        self._parent = None
        self._parentID = None
        self._children = []
        self.content = ''
        self.selectable = False
        self.selected = False
        self.highlight = False
        self.expanded = True
        self.ignore_root = True
        self.sort_function = None
        self.__dict__.update(kwargs)
        if refresh_Branch_ID:
            FragileTree._ID[self._id] = self.__dict__
            try:
                assert(self._parent)
                _Branch._ID[self._parentID]._children.append(self._id)
            except AssertionError:
                pass

class TestApp(nps.NPSAppManaged):
    def main(self):
        F = nps.Form(name = "Project Builder",)
        wgtree = F.add(nps.MLTreeMultiSelect)
        treedata = nps.TreeData(
                content='all',
                selectable=False,
                ignore_root=True)
        f1 = treedata.new_child(
                content='+ Add a New Feature',
                selectable=True,
                selected=True)
        #c2 = treedata.new_child(content='Child 2', selectable=True)
        tf1 = f1.new_child(
                content='+ Add a New Task',
                selectable=True)
        sfe1 = fe1.new_child(
                content='+ Add a New User Story',
                selectable=True)

        gg2 = g1.new_child(content='Great Grand-child 2', selectable=True)
        gg3 = g1.new_child(content='Great Grand-child 3')
        wgtree.values = treedata
        F.edit()
        global RETURN
        RETURN = wgtree.get_selected_objects()




if __name__ == "__main__":
    App = TestApp()
    App.run()
    for v in RETURN:
        print(v)
