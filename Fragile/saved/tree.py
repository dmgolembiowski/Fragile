#!/usr/bin/env python
from pudb import set_trace; set_trace(paused=False)
RETURN = []
ipy = False
import npyscreen
import IPython
import sys

class SelectableTreeLine(npyscreen.TreeLineSelectableAnnotated):
    def calculate_area_needed(self):
        "Need two lines of screen, and any width going"
        return 2,0
    

class TestTree(npyscreen.MLTreeMultiSelect):
    _contained_widgets = SelectableTreeLine
    _contained_widget_height = 2


class TestApp(npyscreen.NPSApp):
    def main(self):
        F = npyscreen.Form(name = "Testing Tree class",)
        #wgtree = F.add(npyscreen.MLTree)
        wgtree = F.add(TestTree)
        treedata = npyscreen.NPSTreeData(content='Fragile', selectable=True, ignoreRoot=False)
        toplvl = treedata.newChild(content="Intuitive Tree UI", selectable=True)
        base_task = toplvl.newChild(content="Add a new Task", selectable=True)
        base_feature = treedata.newChild(content='Add a new Feature', selectable=True, selected=True)
        #g1 = c1.newChild(content='Grand-child 1', selectable=True)
        #g2 = c1.newChild(content='Grand-child 2', selectable=True)
        #g3 = c1.newChild(content='Grand-child 3')
        #gg1 = g1.newChild(content='Great Grand-child 1', selectable=True)
        #gg2 = g1.newChild(content='Great Grand-child 2', selectable=True)
        #gg3 = g1.newChild(content='Great Grand-child 3')
        wgtree.values = treedata
        namespace = {
            'wgtree': 'wgtree = F.add(TestTree)',
            'treedata': "treedata = npyscreen.NPSTreeData(content='Root', selectable=True,ignoreRoot=False)",
            'c1': "c1 = treedata.newChild(content='Child 1', selectable=True, selected=True) ",
            'c2': "c2 = treedata.newChild(content='Child 2', selectable=True) ",
            'g1': "g1 = c1.newChild(content='Grand-child 1', selectable=True) ",
            'g2': "g2 = c1.newChild(content='Grand-child 1', selectable=True) ",
            'g3': "g3 = c1.newChild(content='Grand-child 1', selectable=True) ",
            'gg1': "gg1 = g1.newChild(content='Great Grand-child 1', selectable=True) ",
            'gg2': "gg1 = g1.newChild(content='Great Grand-child 2', selectable=True) ",
            'gg3': "gg1 = g1.newChild(content='Great Grand-child 3') ",
            'wgtree.values': "wgtree.values = treedata ",
        }
        global ipy
        if ipy:
            IPython.embed()
            sys.exit()
        F.edit()
        
        global RETURN
        #RETURN = wgtree.values
        RETURN = wgtree.get_selected_objects()




if __name__ == "__main__":
    try:
        if sys.argv[1]:
            ipy = True
    except IndexError:
        pass
    App = TestApp()
    App.run()   
    for v in RETURN:
        print(v)
