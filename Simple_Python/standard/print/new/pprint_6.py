#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
from pprint_data import data

for width in [80,5]:
    print 'WIDTH =',width
    pprint(data,width=width)
    print