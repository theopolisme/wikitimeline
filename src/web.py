#!/usr/bin/env python

""" This is what is called by the web browser as a cgi script
	E.g., web.py?user=Example&depth=key """

import cgitb
cgitb.enable()

import cgi
import wikitimeline

form = cgi.FieldStorage()
user = form["user"].value
if "depth" in form:
	depth = form["user"].value
else:
	depth = 'all'

data = wikitimeline.User(user,depth=depth)
data.load()

if "raw" in form:
	output = data.raw()
	# !todo make this json
else:
	output = data.pretty()

print output
