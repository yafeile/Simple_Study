#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import sys

sys.stderr.write('repeater.py:starting\n')
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('repeater.py:existing\n')
sys.stderr.flush()