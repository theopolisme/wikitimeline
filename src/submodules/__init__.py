#!/usr/bin/env python

import os
import sys
import glob

# monkey-patching the __import__ functionality to allow for dynamic imports
def import_and_return(*args,**kwargs):
	ret = old_import(*args,**kwargs)
	return ret

old_import = __import__
__builtins__['__import__'] = import_and_return

MODULES = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]
MODULES.remove('__init__')

class Collector():
	def __init__(self,user,depth):
		self.user = user
		if depth == 'all':
			self.depth = 3
		elif depth == 'key':
			self.depth = 2
		elif depth == 'minimal':
			self.depth = 1

	def collect(self):
		userdata = {}
		sys.path.append(os.path.dirname(__file__))
		for modulen in MODULES:
			print "Adding data from {}.".format(modulen)
			module = __import__(modulen)
			if module.DEPTH <= self.depth:
				script = module.JuniorCollector(self.user)
				output = script.raw()
				userdata = dict(userdata.items() + output.items())
			else:
				print "Skipping {}; too detailed for current depth.".format(modulen)
		sys.path.remove(os.path.dirname(__file__))
		self.userdata = userdata

	def output(self):
		return self.userdata
