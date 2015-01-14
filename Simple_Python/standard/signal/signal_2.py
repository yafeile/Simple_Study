#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import signal

def alarm_received(n,stack):
    return

signal.signal(signal.SIGALRM,alarm_received)

signal_to_names = dict(
    (getattr(signal,n),n)
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
    )

for s,name in sorted(signal_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print '%-10s (%2d):' % (name,s),handler