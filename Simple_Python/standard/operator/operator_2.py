#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from operator import *

a = 1
b = 5.0
print 'a=',a
print 'b=',b
for func in (lt,le,eq,ne,ge,gt):
    print '%s(a,b):' % func.__name__,func(a,b)