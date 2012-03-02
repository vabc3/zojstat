# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref
from sqlalchemy.types import Integer, Unicode, Boolean, DateTime
from zojstat.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'UserStat' ]

class UserStat(DeclarativeBase):

	__tablename__ = 'zus'

	id 		= Column(Integer, 	primary_key=True)	#数据库id
	sid		= Column(Integer,	nullable=False)		#提交id
	pid 	= Column(Integer,	nullable=False)		#问题id
	user 	= Column(String(32),nullable=False)		#用户名
	status	= Column(Integer,	nullable=False)		#通过与否
	time	= Column(DateTime,	nullable=False)  	#提交时间
	
	def show(self):
		print "id:",self.id,"|sid:",self.sid,"|pid:",self.pid, \
				"|user:",self.user,"|status",self.status, \
				"|time:",self.time
