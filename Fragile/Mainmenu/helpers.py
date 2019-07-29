from __future__ import annotations
import npyscreen
nps = npyscreen
import threading
import os
import sys
from cursesmenu import CursesMenu, SelectionMenu, curses_menu
from cursesmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
#sys.path.append("/home/david/.local/bin/Fragile/Fragile/")
#from Extensions import FileExplorer
#from .Cursedmenu import CursesMenu, SelectionMenu, curses_menu
#from .Cursedmenu.items import SubmenuItem, CommandItem, MenuItem, FunctionItem
#from .Extensions import FileExplorer
import curses
import json
import IPython
import subprocess
import functools
import datetime
from pathlib import Path

class Handler:
    """
    A class for providing swiss-army knife capabilities. 
    Instances of the Handler class can have any number of
    named parameters passed to them, and the objects made
    will have those attributes.
    
    Likewise, Handler provides two high-utility staticmethods
    for (1) bootstrapping methods onto objects, and (2) 
    generating singleton objects for high-flexibility factory
    objects that stave off garbage collection."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def addmethod(obj, name, func):
        klass = obj.__class__
        subclass = type(klass.__name__, (klass,), {})
        setattr(subclass, name, func)
        obj.__class__ = subclass
    """
    @staticmethod
    def factory(class_name='Self'):
        def wrapper(className=class_name):
            className += f'_{hash(str(random.random()))}'
            eval(f"class {className}:\n    pass")
    """     
    @staticmethod
    def make_dynamic(function):
        cache = {}
        @functools.wraps(function)
        def result(*args, clear_cache=False, ignore_cache=False, skip_cache=False, **kwargs):
            nonlocal cache
            call = (args, tuple(kwargs.items()))
            if clear_cache:
                cache = {}
            if call in cache and not ignore_cache:
                return cache[call]
            res = function(*args, **kwargs)
            if not skip_cache:
                cache[call] = res
                cache[call] = res
            return res
        return result

class FragileProject(FunctionItem):
    each = []
    def __init__(self, name, datastructure, function=lambda: None, args=[]):
        self.name = name
        self.datastructure = datastructure
        self.function = function
        self.args = args
        FragileProject.each.append(self)

    def __str__(self):
        return self.name

    @staticmethod
    def refresh_saved(f):
        FragileProject.each = []
        return f
