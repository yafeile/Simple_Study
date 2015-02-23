#! /usr/bin/env/python
# -*- coding:utf-8 -*-

def my_function(a,b):
    """Return a * b
    >>> my_function(['A','B'],3) #doctest: +NORMALIZE_WHITESPACE
    ['A','B',
     'A','B',
     'A','B',]
     This does not match because of the extra space after the [ in the list.
     >>> my_function(['A','B'],2) #doctest: +NORMALIZE_WHITESPACE
     ['A','B',
     'A','B',]
    """
    return a*b