 #!/usr/bin/env python

""" Returns basic statistics about the user, including edit count, creation date, and log events. """

DEPTH = 1

import config
site = config.site

import dateutil.parser
from datetime import datetime
from time import mktime
from collections import Counter

class JuniorCollector():
	def __init__(self,user):
		self.user = user
		self.process()

	def process(self):
		results = {}

		# Basic data
		basedata = site.users([self.user],prop='registration|editcount|gender').next()
		results['gender'] = basedata['gender'] if 'gender' in basedata else 'unknown'
		results['editcount'] = basedata['editcount']
		results['registration'] = dateutil.parser.parse(basedata['registration'])

		# User rights changes
		rightsevents = site.logevents(title="User:"+self.user,type='rights')
		rightschanges = []
		timeline = []
		for event in rightsevents:
			if event['action'] == 'rights':
				newbase = event['rights']['new'].split(', ')
				new = Counter(newbase)
				old = Counter(event['rights']['old'].split(', '))
				diff = new-old
				if len(list(diff.elements())) > 0:
					rightschanges.append({'type':'rightschange','cur':newbase,'change':'add','rights':list(diff.elements()),'comment':event['comment'],'timestamp':datetime.fromtimestamp(mktime(event['timestamp']))})
				diff2 = old-new
				if len(list(diff2.elements())) > 0:
					rightschanges.append({'type':'rightschange','cur':newbase,'change':'remove','rights':list(diff2.elements()),'comment':event['comment'],'timestamp':datetime.fromtimestamp(mktime(event['timestamp']))})
		results['rightschanges'] = rightschanges
		for change in rightschanges:
			timeline.append(change)

		#!todo block log

		self.results = results
		self.timeline = timeline

	def raw(self):
		return self.results,self.timeline
