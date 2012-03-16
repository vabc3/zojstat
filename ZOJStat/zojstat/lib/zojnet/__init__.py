# -*- coding: utf-8 -*-
import urllib

def getWeb(url):
	f = urllib.urlopen(url)
	data = f.read()
	f.close()
	return data
