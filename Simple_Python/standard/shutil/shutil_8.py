#! /us/bin/env/python
# -*- coding:utf-8 -*-

from shutil import *
from commands import *

print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
rmtree('/tmp/example')
print '\nAFTER:'
print getoutput('ls -rlast /tmp/example')