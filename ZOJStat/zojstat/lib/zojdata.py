# -*- coding: utf-8 -*-
"""maitian data"""

from zojstat.model import DBSession, metadata, SubmissionInfo, ReportInfo
from zojstat.lib.zojnet.sinfo import *
from zojstat.lib.dbdao.SubmissionInfoDao import savesinfo,getmaxsid,getmaxpid as gsmp
from zojstat.lib.dbdao.ProblemInfoDao import savepinfo
from zojstat.lib.zojnet.pinfo import getpid
from logging import getLogger
import time,datetime
import copy
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
			'Compilation Error'		: 'CE',
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
    res 	= DBSession.query(ReportInfo).filter(ReportInfo.user==user)	\
				.order_by(ReportInfo.pid)
    report=[]
    for b in res:
        p=copy.copy(b)
        p.duration=(p.etime-p.btime).__str__()
        if ttable.has_key(p.status):
            p.status=ttable[p.status]
        else:
            p.status=ttable['u']
        if(p.status=='AC'):
            p.ac=True
        else:
            p.ac=False
    	report.append(p)
    passed =1
    return dict(user=user,passed=passed,count=len(report),zuses=report)
