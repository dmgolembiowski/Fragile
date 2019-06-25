#!/usr/bin/env python3
from __future__ import annotations
import npyscreen as nps

class App(nps.NPSAppManaged):
    def onStart(self):
        self.addFormClass("MAIN", MainForm)

class Explorer(nps.BoxTitle, ):
    def __init__(
            self,
            form,
            name=None,
            max_height=8,
            footer=None,
            slow_scroll=False,
            **kwargs):
        self.form = form
        self.name = name
        self.max_height = max_height
        self.footer = footer
        self.slow_scroll = slow_scroll
        self.add_explorer()
        self.__dict__.update(kwargs)

    def add_explorer(self):
        self.form.add(
                nps.FileSelector,
                name=self.name,
                footer=self.footer,
                max_height=self.max_height)


class FileExplorer(nps.Explorer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    @nps.wrapper
    def test_function(scr, *args, **kwargs):
        t = nps.selectFile('~/',)
        nps.notify_confirm(title='Repository', message=t)

    @staticmethod
    def main():
        print(FileExplorer.test_function)

if __name__ == '__main__':
    FileExplorer.main()
