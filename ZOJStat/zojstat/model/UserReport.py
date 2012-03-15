# -*- coding: utf-8 -*-

class UserReport(object):
	pid 	= -1
	status	= -1
	etime	= ''
	btime	= '' 
	count	= 0
	ac		= False
	duration	= 'x'
	
	def __init__(self,pid,status,btime,etime,count):
		self.pid	= pid
		self.status	= status
		self.btime	= btime		
		self.etime	= etime
		self.count	= count


