# -*- coding: utf-8 -*-
from zojstat import model
from zojstat.model import DBSession,ProblemInfo
from sqlalchemy import func
from zope.sqlalchemy.datamanager import mark_changed 

def getmaxpid():
	que=DBSession.query(func.max(ProblemInfo.pid))
	rt	= 0
	if que.scalar() != None :
		rt	= que.scalar()
	return rt;

def getmaxvid():
	que=DBSession.query(func.max(ProblemInfo.cata))
	rt	= 0
	if que.scalar() != None :
		rt	= que.scalar()
	return rt;
	
def _savepinfo(data):
    t	= ProblemInfo.__table__.insert(data.__dict__) \
    		.prefix_with("ignore")
    w=DBSession.connection().execute(t)
	
def savepinfo(data):
    if type(data)==list:
	    for item in data:
	    	_savepinfo(item)
    else:
        _savepinfo(data)
    mark_changed(DBSession())
	
   
