# -*- coding: utf-8 -*-
"Model of ProblemInfo"
from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import  relation, backref
from zojstat.model import DeclarativeBase

__all__ = [ 'ProblemInfo' ]

class ProblemInfo(DeclarativeBase):

    __tablename__ = 'pinfo'

    pid		= Column(Integer, primary_key=True)		#数据库id
    title 	= Column(String(64), nullable=False)	#用户名
    cata	= Column(Integer, nullable=False)	#分类
	
    def __repr__(self):
        return "<Pinfo pid='%s' title='%s' cata='%s'>" % \
        (self.pid,self.title,self.cata)
