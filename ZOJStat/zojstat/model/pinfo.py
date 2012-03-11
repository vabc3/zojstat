# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref
from sqlalchemy.types import Integer, Unicode, Boolean, DateTime
from zojstat.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'Pinfo' ]

class Pinfo(DeclarativeBase):

	__tablename__ = 'pinfo'

	pid		= Column(Integer, 	primary_key=True)	#数据库id
	title 	= Column(String(64),nullable=False)		#用户名
	cata	= Column(String(64),nullable=False)		#分类
	
	def __repr__(self):
		return "<Pinfo pid='%s' title='%s' cata='%s'>" % \
		(self.pid,self.title,self.cata)
