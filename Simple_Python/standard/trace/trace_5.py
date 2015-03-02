#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import trace
from recurse_1 import recurse

tracer = trace.Trace(count=True,
                                 trace=False,
                                 outfile='trace_report.dat')
tracer.runfunc(recurse,2)

report_tracer = trace.Trace(count=False,
                                             trace=False,
                                             infile='trace_report.dat')
results = tracer.results()
results.write_results(summary=True,
                                coverdir='/tmp')