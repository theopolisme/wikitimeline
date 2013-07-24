 #!/usr/bin/env python

""" Returns basic statistics about the user, including edit count, creation date, and block log. """

DEPTH = 1

import config
site = config.site

class JuniorCollector():
	def __init__(self,user):
		self.user = user

	def raw(self):
		return {'sample':site.Pages['Example']}
