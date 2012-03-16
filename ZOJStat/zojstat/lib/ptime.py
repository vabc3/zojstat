# -*- coding: utf-8 -*-
import time

class ptime(object):
    def __init__(self):
        self.ol=time.time()
		
    def gap(self):
        return time.time()-self.ol
