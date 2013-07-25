#!/usr/bin/env python

from datetime import datetime
import inflect

INFLECTOR = inflect.engine()
NOW = datetime.now()

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

def prettify(user,userdata):
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

	output += "{0} currently {1} the {2} userright{3}.".format(
		singular.capitalize(),
		has,
	output += "{0} currently {1} the {2} userright{3}. ".format(
		INFLECTOR.singular_noun('they').capitalize(),
		'have' if INFLECTOR.thegender == 'gender-neutral' else 'has',
		andlist(userdata['rightschanges'][0]['cur']),
		"" if len(userdata['rightschanges'][0]['cur']) == 1 else "s")

	return output
