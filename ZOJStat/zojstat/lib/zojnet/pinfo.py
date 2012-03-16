# -*- coding: utf-8 -*-
from zojstat.lib.dbdao.ProblemInfoDao import *
from zojstat.lib.zojnet import *
from sgmllib import SGMLParser

base1	= "http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber="

class Parser(SGMLParser):
	td		= 0
	a		= 0
	coll	= []  
	us		= None
	
	def __init__(self):
		SGMLParser.__init__(self)
		self.td		= 0
		self.coll	= []  
		self.us		= None
	
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
		elif self.td=="problemId" :
			self.us		= ProblemInfo()
			self.us.pid	= text
		elif self.td=="problemStatus" :
			self.coll.append(self.us)
			self.td=0
		elif self.td=="problemTitle" :
			self.us.title	= text


def getvol(vid):
    print 'vid',vid
    dat	= getWeb(base1+str(vid))
    pas = Parser()
    pas.feed(dat)
    col	= pas.coll
    print col
    if(len(col)>0):
        col.reverse()
        col.pop()
        col.reverse()
    for ea in col:
        ea.pid=int(ea.pid)
        ea.cata=vid
    return col
	
def getpid(pid,cb):
    while getmaxpid()<pid:
        cb(getvol(getmaxvid()+1))
#        break
