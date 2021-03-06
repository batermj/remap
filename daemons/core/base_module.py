import os
import sys
import logging
import time

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

import lib.remap_utils as remap_utils
import lib.remap_constants as remap_constants
from lib.remap_utils import RemapException

class WorkerBase(object):
    def __init__( self, app, appconfig, workdata ):
        self.app = app
        self.appconfig = appconfig
        self.workdata = workdata
        self.jobid = workdata["jobid"]
        self.remaproot = appconfig["remaproot"]
        self.progress = 0

    def module_manages_progress( self ):
        return False


