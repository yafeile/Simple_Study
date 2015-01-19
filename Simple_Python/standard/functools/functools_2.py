#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import functools

def myfunc(a,b=2):
    """Docstring for myfunc()."""
    print '  called myfunc with:',(a,b)
    return

def show_details(name,f,is_partial=False):
    """Show details of a callable object."""
    print '%s:' % name
    print ' object:',f
    print ' __name__:',
    try:
        print f.__name__
    except AttributeError:
        print ' (no __name__)'
    print ' __doc__',repr(f.__doc__)
    print
    return

show_details('myfunc',myfunc)
myfunc('a',3)
print

p1 = functools.partial(myfunc,b=4)
show_details('raw wrapper',p1)

print 'Updating wrapper:'
print ' assign:',functools.WRAPPER_ASSIGNMENTS
print ' update:',functools.WRAPPER_UPDATES
print

functools.update_wrapper(p1,myfunc)
show_details('update_wrapper',p1)