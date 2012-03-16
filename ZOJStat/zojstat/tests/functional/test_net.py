# -*- coding: utf-8 -*-

from nose.tools import eq_
from zojstat.lib.zojnet.pinfo import *
from zojstat.lib.dbdao.ProblemInfoDao import *

def test_1_certain():
    "找到特定的题"
    cert=2335
    eq_(True,getmaxvid()<cert)
    getpid(cert,savepinfo)
    #eq_(True,getmaxvid()>=cert)
