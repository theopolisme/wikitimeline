#!/usr/bin/env python

from datetime import datetime

NOW = datetime.now()

def prettify(user,userdata):
	"""Given a dict of data, returns prettified unicode!"""
	output = ""
	output += ("{0} has been a Wikipedian for {1:,d} days (since {2}), accruing a total of "
			"{3:,d} edits and counting.").format(
			user,
			(NOW-userdata['registration'].replace(tzinfo=None)).days,
			userdata['registration'].strftime("%d %B %Y"),
			userdata['editcount']
			)
		#{gender} currently has the {permissions} userrights{plur}."
	return output
