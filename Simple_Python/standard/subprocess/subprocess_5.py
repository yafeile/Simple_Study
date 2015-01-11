#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import subprocess

try:
    output = subprocess.check_output('echo to stdout;echo to stderr 1>&2;exit 1',shell=True,)
except subprocess.CalledProcessError as err:
    print 'ERROR:',err
else:
    print 'Have %d bytes in output' % len(output)
    print output