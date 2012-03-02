# -*- coding: utf-8 -*-
"""maitian data"""

import urllib
import logging
import re
from sgmllib import SGMLParser
from zojstat.model.userstat import UserStat

#from zojstat.lib.app_globals import Globals

log 	= logging.getLogger(__name__)
base1	= "http://acm.zju.edu.cn/onlinejudge/showRuns.do?contestId=1&search=true&firstId=-1&lastId="
base2	= "&problemCode=&handle="
base3	= "&idStart="
ac		= re.compile(r"Accept")
nex		= re.compile(".*Next\((\d*)\).*")

class Parser(SGMLParser):
	td		= 0
	a		= 0
	coll	= []  
	us		= None

	ne		= -1
	
	def __init__(self):
		SGMLParser.__init__(self)
		self.td		= 0
		self.coll	= []  
		self.us		= None

	def start_a(self,attrs):
		tdc = [v for k, v in attrs if k=='href']
		if tdc:		
			ma	= nex.match(tdc[0])
			if ma:
#				log.debug(ma.group(1))
				self.ne=ma.group(1)
	
	def start_td(self,attrs):
		tdc = [v for k, v in attrs if k=='class'] 
		if tdc:
			self.td=tdc[0]
			#print self.td
	
	def end_td(self):
		self.td=0
	
	def handle_data(self,text):
		if self.td==0 :					
			pass
		elif self.td=="runId" :
			self.us		= UserStat()
			self.us.sid	= text
		elif self.td=="runUserName" :
			self.coll.append(self.us)
		elif self.td=="runSubmitTime" :
			self.us.time	= text
		elif self.td=="runJudgeStatus" :
			if re.search(ac,text):
				self.us.status	= 0
			else:
				self.us.status	= 1
		elif self.td=="runProblemId"	 :
			self.us.pid		= text
       
class ZOJNet(object):
	@staticmethod
	def getWeb(url):
		f = urllib.urlopen(url)
		data = f.read()
		f.close()
		return data
	
	@staticmethod
	def querya(user,lid,startid):
		log.debug("qa:"+str(lid))
		dat	= ZOJNet.getWeb(base1+str(lid)+base2+user+base3+str(startid))
		pas = Parser()
		pas.feed(dat)
		col	= pas.coll
		if(len(col)>0):
			col.reverse()
			col.pop()
			col.reverse()
		
		return (pas.ne,col)
		
	@staticmethod
	def query(user,startid):
		log.debug("NetQ:"+user)
		
		(pos,col)=ZOJNet.querya(user,-1,startid)
		cot=col
		while pos!=-1 :
			(pos,col)=ZOJNet.querya(user,pos,startid)
			cot.extend(col)
		for pt in cot:
			pt.user=user
		log.debug("Total:"+str(len(cot)))
		return cot
		
		

