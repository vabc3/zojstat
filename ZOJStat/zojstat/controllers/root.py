# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from zojstat import model
from zojstat.model import DBSession, metadata
from zojstat.lib.base import BaseController
from zojstat.controllers.error import ErrorController
from zojstat.lib.zojdata import updateuser, gaindata
import logging

__all__ = ['RootController']
logger 	= logging.getLogger(__name__)

class RootController(BaseController):
	error = ErrorController()

	@expose('zojstat.templates.index')
	def index(self):
		"""Main page."""
		return dict()
		
	@expose('zojstat.templates.query')		
	def query(self,user):
		rem='?'
		if request.remote_addr != None:
			rem = request.remote_addr
		logger.info(rem+" Q:user");
		updateuser(user)
		return gaindata(user)
