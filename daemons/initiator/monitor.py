import os
import sys
import logging
import time

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

import lib.remap_utils as remap_utils
import lib.remap_constants as remap_constants
from lib.remap_utils import RemapException

logging.basicConfig( level=logging.INFO ) 
logger = logging.getLogger("Monitor")

class Monitor(object):
    def __init__(self, rootdir):
        self.rootdir = os.path.abspath( rootdir )
        self.appsdir = os.path.join( self.rootdir, "app" )
        self.jobsdir = os.path.join( self.rootdir, "job" )
        self.datadir = os.path.join( self.rootdir, "data" )
        self.nodes = {}

    def list_apps( self ):
        apps = []
        for root, dirs, files in os.walk( self.appsdir ):
            for f in files:
                if f == "appconfig.json":
                    apps.append( os.path.relpath(root, self.appsdir) )
        return apps

    def list_all_jobs( self ):
        jobs = []
        for root in os.listdir( self.jobsdir ):
            jobs.append( root )
        return jobs

    def list_jobs( self ):
        return {"status":self.job_status,"jobid":self.jobid,"type":self.jobtype,"priority":self.priority,"parallellism":self.parallellism,
            "tasks":len(self.tasks), "allocated":len(self.allocatedtasks), "completed":len(self.completedtasks), "rejected":len(self.rejectedtasks)}

    def list_nodes( self ):
        return self.nodes

    def cancel_job( self ):
        pass

