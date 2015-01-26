#! /us/bin/env/python
# -*- coding:utf-8 -*-

import dircache
import os

path = '/tmp'
file_to_create = os.path.join(path,'pymotw_tmp.txt')

# Look at the directory contents
first = dircache.listdir(path)

# Create the new file
open(file_to_create,'wt').close()

# Rescan the directory
second = dircache.listdir(path)

# Remove the file we created
os.unlink(file_to_create)

print 'Identical :',first is second
print 'Equal     :',first == second
print 'Difference:',list(set(second) - set(first))