#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import collections

c=collections.Counter()
print "Initial:",c
c.update("abcdaab")
print "Sequence:",c
c.update({"a":1,"d":5,"b":2})
print "Dict:",c