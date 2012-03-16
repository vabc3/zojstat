# -*- coding: utf-8 -*-
"""NET data"""
 
import logging
import re
from zojstat.lib.zojnet import *
from sgmllib import SGMLParser
from zojstat.model import SubmissionInfo
#from zojstat.lib.app_globals import Globals

__all__	= ['query']

log 	= logging.getLogger(__name__)
base1	= "http://acm.zju.edu.cn/onlinejudge/showRuns.do?contestId=1&search=true&firstId=-1&lastId="
base2	= "&problemCode=&handle="
base3	= "&idStart="
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
			self.us		= SubmissionInfo()
			self.us.sid	= text
		elif self.td=="runUserName" :
			self.coll.append(self.us)
		elif self.td=="runSubmitTime" :
			self.us.time	= text
		elif self.td=="runJudgeStatus" :
			self.us.status	= " ".join(text.split())
		elif self.td=="runProblemId"	 :
			self.us.pid		= text
       
def querya(user,lid,startid):
#		log.debug("qa:"+str(lid))
	dat	= getWeb(base1+str(lid)+base2+user+base3+str(startid))
	pas = Parser()
	pas.feed(dat)
	col	= pas.coll
	if(len(col)>0):
		col.reverse()
		col.pop()
		col.reverse()
	for ea in col:
		ea.sid=int(ea.sid)
		ea.pid=int(ea.pid)
	return (pas.ne,col)
	
def query(user,startid,cb):
	log.debug("NetQ:"+user)
	
	(pos,col)=querya(user,-1,startid)
	for pt in col:
		pt.user=user
	cb(col)

	while pos!=-1 :
		(pos,col)=querya(user,pos,startid)
		for pt in col:
			pt.user=user
		cb(col)
