# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref
from sqlalchemy.types import Integer, Unicode, Boolean, DateTime
from zojstat.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'UserStat' ]

class SubmissionInfo(DeclarativeBase):

    __tablename__ = 'sinfo'

    id 		= Column(Integer, primary_key=True)		#数据库id
    sid		= Column(Integer, nullable=False)		#提交id
    pid 	= Column(Integer, nullable=False)		#问题id
    user 	= Column(String(32), nullable=False)	#用户名
    status	= Column(String(32), nullable=False)	#通过与否
    time	= Column(DateTime, nullable=False, 
                default='0000-00-00 00:00:00')		#提交时间
	
    def __repr__(self):
        return "<SubmissionInfo id=%d sid=%d pid=%d " \
                "user=%s status=%s time=%s>" % \
        (self.id if(self.id) else -1,self.sid,self.pid,self.user,self.status,self.time)
