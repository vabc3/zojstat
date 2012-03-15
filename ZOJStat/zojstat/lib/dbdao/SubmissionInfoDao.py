# -*- coding: utf-8 -*-
from zojstat.model import DBSession
from zojstat.model import SubmissionInfo

def getmaxsid(user):
	que=DBSession.query(SubmissionInfo).filter(SubmissionInfo.user==user). \
				order_by(SubmissionInfo.sid.desc()).first()
	rt	= 0
	if que != None :
		rt	= que.sid
	return rt;
	
def savesinfo(data):
    try:
    	t=SubmissionInfo.__table__.insert(data.__dict__)
    	t=t.prefix_with("ignore")
    	DBSession.execute(t)
        DBSession.flush()
    except Exception:
        print 'exc'
        DBSession.rollback()
    
