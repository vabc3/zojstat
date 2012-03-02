# -*- coding: utf-8 -*-
"""maitian data"""

import logging
from zojstat import model
from zojstat.model import DBSession, metadata
from zojstat.model.userstat import UserStat
from zojstat.model.userreport import UserReport
from zojstat.lib.zojnet import ZOJNet

log = logging.getLogger(__name__)

class ZOJStatController(object):
	@staticmethod
	def updateuser(user):
		log.debug("Updating:"+user)
		que	= DBSession.query(UserStat).filter(UserStat.user==user). \
				order_by(UserStat.sid.desc()).first()
		sd=1
		if que != None :
			sd=que.sid+1
		log.debug(sd)
#		col=[]
		col	= ZOJNet.query(user,sd)
		for us in col:
			DBSession.add(us)

	@staticmethod
	def gaindata(user):
		log.debug("Query:"+user)
		usds 	= DBSession.query(UserStat).filter(UserStat.user==user). \
					order_by(UserStat.sid)
		report	= []
		
		dic	= dict()
		
		for usd in usds:
			if dic.has_key(usd.pid):
				qt=dic[usd.pid]
				if usd.status == 0 :
					qt.status = 0
				qt.etime=usd.time
				qt.count=qt.count+1
				dic[usd.pid]=qt
			else:
				ur	= UserReport(usd.pid,usd.status,usd.time,usd.time,1)
				dic[usd.pid]=ur
		for p in dic.values():
			report.append(p)
		
		report.sort(lambda x,y:cmp(x.pid,y.pid))
		
#		print html.tags.image('/images/rss.png', 'rss syndication')
		return dict(user=user,count=len(report),zuses=report)
