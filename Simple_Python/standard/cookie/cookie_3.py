# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import Cookie
import datetime

def show_cookie(c):
	print c
	for key,morsel in c.iteritems():
		print
		print 'key =',morsel.key
		print 'value =',morsel.value
		print 'coded_value =',morsel.coded_value
		for name in morsel.keys():
			if morsel[name]:
				print ' %s = %s' % (name,morsel[name])

c = Cookie.SimpleCookie()
#A cookie with a value that has to be encoded to fit into the header
c['encoded_value_cookie'] = '"cookie_value"'
c['encoded_value_cookie']['comment'] = 'Value has escaped quotes'

#A cookie that only applies to part of a site
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

#A cookie that expires in 5 minutes
c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age']['max-age'] = 300

#A cookie that expires at a specific time
c['expires_at_time'] = 'cookie_value'
time_to_live = datetime.timedelta(hours=1)
expires = datetime.datetime(2014,12,16,17,12,10) + time_to_live

#Date format:wdy,DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a,%d %b %Y %H:%M:%S')
c['expires_at_time']['expires'] = expires_at_time
show_cookie(c)