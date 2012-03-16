# -*- coding: utf-8 -*-
from zojstat.model import DBSession,SubmissionInfo
from zojstat import model
import transaction
import traceback,sys
from zope.sqlalchemy.datamanager import mark_changed 
from sqlalchemy import func

def getmaxpid():
	que=DBSession.query(func.max(SubmissionInfo.pid))
	rt	= 0
	if que.scalar() != None :
		rt	= que.scalar()
	return rt;

def getmaxsid(user):
	que=DBSession.query(SubmissionInfo).filter(SubmissionInfo.user==user). \
				order_by(SubmissionInfo.sid.desc()).first()
	rt	= 0
	if que != None :
		rt	= que.sid
	return rt;
	
def _savesinfo(data):
    t	= SubmissionInfo.__table__.insert(data.__dict__) \
    		.prefix_with("ignore")
    w=DBSession.connection().execute(t)
	
def savesinfo(data):
    if type(data)==list:
	    for item in data:
	    	_savesinfo(item)
    else:
        _savesinfo(data)
    mark_changed(DBSession())
	
   
