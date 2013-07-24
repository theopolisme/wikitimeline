# config.py

import mwclient
import password

site = mwclient.Site('en.wikipedia.org')
site.login(password.username,password.password)
