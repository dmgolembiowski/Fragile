# encoding: utf-8
"""Terminal-based IPython entry point.
"""
#-----------------------------------------------------------------------------
#  Copyright (c) 2012, IPython Development Team.
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
import sys
from Fragile import Application

app = Application()
sys.exit(app.start_fragile())
