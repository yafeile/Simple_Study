#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import gc
import pprint

class Graph(object):
    def __init__(self,name):
        self.name = name
        self.next = None
    def set_next(self,next):
        print 'Linking nodes %s.next = %s' %(self,next)
        self.next = next
    def __repr__(self):
        return '%s (%s)' % (self.__class__.__name__,self.name)

# Construct a graph cycle
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Remove references to the graph nodes in this modules's namespace
one = two = three = None

# Show the effect of garbage collection
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:',n
print 'Remaining Garbage:',
pprint.pprint(gc.garbage)