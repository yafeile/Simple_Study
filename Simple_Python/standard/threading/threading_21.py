# -*- coding:utf-8 -*-
#! /usr/bin/env/python

import threading
import logging
import time
import random

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s (%(threadName)-2s) %(message)s',
)

class ActivePool(object):
	def __init__(self):
		super(ActivePool,self).__init__()       #重载自身的__init__()方法,reload self method
		self.active = []
		self.lock = threading.Lock()

	def makeActive(self,name):
		with self.lock:
			self.active.append(name)
			logging.debug('Running {0} at {1}'.format(self.active,time.ctime()))

	def makeInactive(self,name):
		with self.lock:
			self.active.remove(name)
			logging.debug('Running {0} at {1}'.format(self.active,time.ctime()))

def worker(s,pool):
	logging.debug('Waiting to join the pool at {0}'.format(time.ctime()))
	with s:
		name = threading.currentThread().getName()
		pool.makeActive(name)
		time.sleep(0.1)
		pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
	t = threading.Thread(target=worker,name=str(i),args=(s,pool))
	t.start()