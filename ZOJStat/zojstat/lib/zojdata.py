# -*- coding: utf-8 -*-
"""maitian data"""

import logging
from zojstat import model
from zojstat.model import DBSession, metadata, SubmissionInfo, UserReport
from zojstat.lib.zojnet import ZOJNet
from zojstat.lib.dbdao.SubmissionInfoDao import savesinfo,getmaxsid

log = logging.getLogger(__name__)

def updateuser(user):
    log.debug("Updating:"+user)
    que	= getmaxsid(user)
    sd=que+1
    log.debug(sd)
#		col=[]
    col	= ZOJNet.query(user,sd)
    for us in col:
        DBSession.add(us)

def gaindata(user):
    log.info("Query:"+user)
    usds 	= DBSession.query(SubmissionInfo).filter(SubmissionInfo.user==user). \
				order_by(SubmissionInfo.sid)
    report	= []
    passed	= 0
    dic		= dict()

    for usd in usds:
        if dic.has_key(usd.pid):
            qt=dic[usd.pid]
            if usd.status == 0 and qt.status != 0:
#					print qt.pid
                qt.status = 0
                passed+=1

            qt.etime=usd.time
            qt.count=qt.count+1
            dic[usd.pid]=qt
        else:
            ur	= UserReport(usd.pid,usd.status,usd.time,usd.time,1)
            if usd.status == 0:
                passed+=1
            dic[usd.pid]=ur
    for p in dic.values():
        report.append(p)
    report.sort(lambda x,y:cmp(x.pid,y.pid))
    return dict(user=user,passed=passed,count=len(report),zuses=report)
