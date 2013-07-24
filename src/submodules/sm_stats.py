 #!/usr/bin/env python

""" Returns basic statistics about the user, including edit count, creation date, and block log. """

DEPTH = 1

class JuniorCollector():
	def __init__(self,user):
		self.user = user

	def raw(self):
		return {'sample':'data'}
