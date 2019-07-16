#!/usr/bin/env python3
from __future__ import annotations
import npyscreen as nps
import curses
import json
import random

class Self:
    def __init__(this, superclass=None):
        name = "_"+str(hash(random.random()))
        if superclass is None:
            this = eval(f"class {name}:\n    pass")
        else:
            this = eval(f"class {name}({superclass}):\n    pass")

class Fwidget:
    """`Fwidget` is a namespace of methods that return objects
    facading as a class.

    PARAMETERS
    ----------
    None

    METHODS
    -------
    `Fwidget.Textbox()`: A static method for adding an editable
            textbox to the npyscreen form provided as an arg.
            Type `help(FWidget.Textbox)` for a list of params."""
    @staticmethod
    def Textbox(
            form,
            _value_list,
            _name="Textbox",
            _max_height=6,
            _footer="Press [i|o] to edit | ctrl-p: [↑] | ctrl-n: [↓]",
            _slow_scroll=False):
        return form.add(npyscreen.MultiLineEditableBoxed,
                max_height=_max_height,
                name=_name,
                footer=_footer,
                values=_value_list,
                slow_scroll=_slow_scroll)


class FragileForm:
    def __init__(
            self,
            name,
            superclass=None,
            **kwargs):
        self = Self(superclass=superclass)
        for kw in kwargs.keys():
            exec(f"self.kw=kwargs[kw]")
        self.name = name

class NewScreen(nps.ActionForm):
    def __init__(self, *widgets):
        for widget in widgets:
            try:
                self.add_widget(**widget.__dict__)
            except Exception as e:
                raise(e)

class SavedScreen(NewScreen):
    def __init__(self, *widgets, **kwargs):
        super().__init__(self, *widgets)
        self.__dict__.update(kwargs)


class Polyscreen(nps.NPSAppManaged):
    def __init__(self):
        self.forms = []

    def onStart(self, *forms):
        self.collect(forms)

    def collect(self, *forms):
        for form in forms:
            try:
                assert(form.isProtoForm)
            except AssertionError:
                base_attrs = {
                        'f_id': form.f_id,
                        'FormClass': form.FormClass,
                    }
                keywords = form.__dict__
                for attr in base_attrs.keys():
                    keywords.pop(attr)
                self.addForm(
                        f_id=form.f_id,
                        FormClass=form.FormClass,
                        **keywords)
























