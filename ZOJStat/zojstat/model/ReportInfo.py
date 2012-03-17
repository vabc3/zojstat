# -*- coding: utf-8 -*-
"Model of ReportInfo"
from sqlalchemy import Column, Integer, String
from zojstat.model import DeclarativeBase
from sqlalchemy.types import Integer, Unicode, Boolean, DateTime

__all__ = [ 'ReportInfo' ]

class ReportInfo(DeclarativeBase):

    __tablename__ = 'rinfo'

    pid		= Column(Integer, primary_key=True)		#数据库id
    cata	= Column(Integer, nullable=False)	#分类
    user 	= Column(String(32), nullable=False)	#用户名
    title 	= Column(String(64), nullable=False)	#题名
    status  = Column(String(64), nullable=False)
    count	= Column(Integer, nullable=False)
    btime	= Column(DateTime, nullable=False)
    etime	= Column(DateTime, nullable=False)
    ac		= Column(Integer, nullable=False)
	
    def __repr__(self):
        return "<Pinfo pid='%s' title='%s' cata='%s'>" % \
        (self.pid,self.title,self.cata)
