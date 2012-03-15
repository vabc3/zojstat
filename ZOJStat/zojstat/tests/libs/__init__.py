# -*- coding: utf-8 -*-
from zojstat.model import DBSession

def teardown(self):
    """Finish model test fixture."""
    DBSession.rollback()
