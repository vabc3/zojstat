# -*- coding: utf-8 -*-
"""Test suite for the TG app's models"""
from nose.tools import eq_
from zojstat import model
from zojstat.tests.models import ModelTest

class TestPinfo(ModelTest):
	"Pinfo Model"
	klass	= model.Pinfo
	attrs	= dict(
				pid = 133,
				title ='fdsj',
				cata  ='w'
			)
	def test_obj_creation_username(self):
		"""Mattest"""
		eq_(self.obj, 1331)

