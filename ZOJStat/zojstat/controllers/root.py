# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from zojstat.model import DBSession, metadata
from zojstat.lib.base import BaseController
from zojstat.controllers.error import ErrorController
from zojstat.lib.zojdata import updateuser, gaindata
from logging import getLogger

__all__ = ['RootController']
logger 	= getLogger(__name__)

class RootController(BaseController):
	error = ErrorController()

	@expose('zojstat.templates.index')
	def index(self):
		"""Main page."""
		return dict(time='2')
		
	@expose('zojstat.templates.query')		
	def query(self,user):
		"Query Page"
		rem=request.remote_addr
		if rem== None:
			rem = '?'
		logger.info(rem+" Q:user");
		updateuser(user)
		return gaindata(user)
