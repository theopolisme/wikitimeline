#!/usr/bin/env python

import submodules

class User:
	def __init__(self,username):
		self.username = username

	def load(self,depth='all'):
		"""Calls all the necessary submodules to generate
		user's contribution history.

		Depth is used to specify how detailed the history
		should be. 'all' (default), 'key' (only key events),
		or 'minimal' (only user statistics)
		"""
		userdata = {}
		collector = submodules.Collector(user=self.username,depth=depth)
		collector.collect()
		self.userdata = collector.output()


	def raw(self):
		"""Returns a raw dict of data points from the
		user's contribution history."""
		return self.userdata

	def pretty(self):
		"""Returns natural language summary of the user's
		contribution history."""


if __name__ == '__main__':
	import sys
	data = User(username=sys.argv[1])
	data.load(depth=sys.argv[2])
	print data.raw()
