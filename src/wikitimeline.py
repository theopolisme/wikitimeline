#!/usr/bin/env python

import mwclient
from submodules import *

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

	def raw(self):
		"""Returns a raw list of data points from the
		user's contribution history."""

	def pretty(self):
		"""Returns natural language summary of the user's
		contribution history."""
