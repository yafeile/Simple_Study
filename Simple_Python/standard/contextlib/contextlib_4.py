#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import contextlib

@contextlib.contextmanager
def make_context():
    print ' entering'
    try:
        yield {}
    except RuntimeError, err:
        print ' ERROR:',err
    finally:
        print ' exiting'
print 'Normal:'
with make_context() as value:
    print ' inside with statement:',value

print '\nHandled error:'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print '\nUnhandled error:'
with make_context() as value:
    raise ValueError('this exception is not handled')