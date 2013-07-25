#!/usr/bin/env python

import itertools
import random
from datetime import datetime
import collections
import string
import inflect

INFLECTOR = inflect.engine()
NOW = datetime.now()

class CapsFormatter(string.Formatter):
	def convert_field(self, value, conversion):
		# do any conversion on the resulting object
		if conversion is None:
			return value
		elif conversion == 's':
			return str(value)
		elif conversion == 'r':
			return repr(value)
		elif conversion == 'c':
			return value.capitalize()
		raise ValueError("Unknown conversion specifier {0!s}".format(conversion))
formatter = CapsFormatter()

def andlist(list):
	"""A more advanced list -> string printer
	(now with 140 times more 'and'!)
	"""
	if len(list) == 2:
		return ' and '.join(list)
	elif len(list) >= 3:
		string = ""
		for i,item in enumerate(list):
			if i != len(list)-1:
				string += item+", "
			else:
				string += "and "+item
		return string
	else:
		return ", ".join(list) # okay, we just don't know what to do (also works for 1-item lists).

def prettify(user,userdata,timeline):
	"""Given a dict of data, returns prettified unicode!"""
	gender = userdata['gender']
	global INFLECTOR
	if gender == "male":
		INFLECTOR.gender('masculine')
	elif gender == "female":
		INFLECTOR.gender('feminine')
	else:
		INFLECTOR.gender('gender-neutral')


	output = ""
	output += ("{0} has been a Wikipedian for {1:,d} days (since {2}), accruing a total of "
			"{3:,d} edits and counting. ").format(
			user,
			(NOW-userdata['registration'].replace(tzinfo=None)).days,
			userdata['registration'].strftime("%d %B %Y"),
			userdata['editcount']
			)

	output += "{0} currently {1} the {2} userright{3}. ".format(
		INFLECTOR.singular_noun('they').capitalize(),
		'have' if INFLECTOR.thegender == 'gender-neutral' else 'has',
		andlist(userdata['rightschanges'][0]['cur']),
		"" if len(userdata['rightschanges'][0]['cur']) == 1 else "s"
		)

	output += generate_timeline(user,timeline)

	return output

def generate_timeline(user,timeline):
	"""Given a list of dicts (that include the value "timestamp"), mixes them up
	all relative to one another and outputs them. Harder than it seems.
	"""
	output = ''
	timeline = sorted(timeline, key=lambda item: item["timestamp"])
	for event in timeline:
		date = event['timestamp']
		if event['type'] == 'rightschange': # this is therefore a userrights modification
			if event['rights'][0] != "": # funkiness
				printme = random.choice(["On {date}, {user} {rmadd} the {permissions} group{plur}. ",
										"{user!c} {rmadd} the {permissions} group{plur} on {date}. "])
				output += formatter.format(printme,
										date=date.strftime("%d %B %Y"),
										user=random.choice([user+" was",INFLECTOR.singular_noun('they')+(" were" if INFLECTOR.thegender == "gender-neutral" else " was")]),
										permissions=andlist(event['rights']),
										rmadd="removed from" if event['change'] == "remove" else "added to",
										plur="s" if len(event['rights']) > 1 else "")
	return output
