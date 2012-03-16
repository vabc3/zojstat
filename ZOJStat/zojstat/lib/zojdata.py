# -*- coding: utf-8 -*-
"""maitian data"""

from zojstat.model import DBSession, metadata, SubmissionInfo, UserReport
from zojstat.lib.zojnet.sinfo import *
from zojstat.lib.dbdao.SubmissionInfoDao import savesinfo,getmaxsid,getmaxpid as gsmp
from zojstat.lib.dbdao.ProblemInfoDao import savepinfo
from zojstat.lib.zojnet.pinfo import getpid
from logging import getLogger
import time,datetime
__all__=['updateuser']
log = getLogger(__name__)
sac	= 'Accepted'
format="%Y-%m-%d %H:%M:%S"
ttable	= {'Accepted'				: 'AC',
			'Presentation Error'	: 'PE',
			'Wrong Answer'			: 'WA',
			'Time Limit Exceeded'	: 'TLE',
			'Memory Limit Exceeded'	: 'MLE',
			'Output Limit Exceeded'	: 'OLE',
			'Non-zero Exit Code'		: 'NEC',
			'Compile Error'			: 'CE',
			'Segmentation Fault'	: 'SF',
			'u'						: '??',
			}


def updateuser(user):
    log.debug("Updating:"+user)
    que	= getmaxsid(user)
    sd=que+1
    log.debug("maxid="+str(sd))
    query(user,sd,savesinfo)
    getpid(gsmp(),savepinfo)


def gaindata(user):
    log.info("Query:"+user)
    usds 	= DBSession.query(SubmissionInfo) 		\
				.filter(SubmissionInfo.user==user)	\
				.order_by(SubmissionInfo.sid)
    report	= []
    passed	= 0
    dic		= dict()

    for usd in usds:
        if dic.has_key(usd.pid):
            qt=dic[usd.pid]

            if usd.status == sac and qt.status != sac:
                passed+=1
                qt.ac =True;
            if qt.status !=sac :
                qt.status = usd.status
            qt.etime=usd.time
            qt.count=qt.count+1
            dic[usd.pid]=qt
        else:
            ur	= UserReport(usd.pid,usd.status,usd.time,usd.time,1)
            if usd.status == sac:
            	ur.ac	= True;
                passed+=1
            dic[usd.pid]=ur
    for p in dic.values():
    	p.duration=(p.etime-p.btime).__str__()
        if ttable.has_key(p.status):
    		p.status=ttable[p.status]
    	else:
    		p.status=ttable['u']
        report.append(p)
    report.sort(lambda x,y:cmp(x.pid,y.pid))
    return dict(user=user,passed=passed,count=len(report),zuses=report)
