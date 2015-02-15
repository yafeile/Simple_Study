#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import imaplib
import imaplib_1

c = imaplib_1.open_connection()
try:
    typ,data = c.select('INBOX')
    print typ,data
    num_msgs = int(data[0])
    print 'There are %d messages in INBOX' % num_msgs
finally:
    #c.close()
    c.logout()