#! /usr/bin/env/python
# -*- coding:utf-8 -*-

from Queue import Queue
from threading import Thread
import time
import urllib
import urlparse
import feedparser

#Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

#A real app wouldn't use hard-coded data...
feed_urls = ['http://rss.sina.com.cn/news/marquee/ddt.xml',]

def downloadEnclosures(i,q):
    """This is the worker thread function.
    It processes items in the queue one after another.
    These daemon threads go into an infinite loop,and only exit when the main thread ends.
    """
    while True:
    	print '%s:Looking for the next enclosure' % i
    	url = q.get()
    	parsed_url = urlparse.urlparse(url)
    	print '%s:Downloading:' % i,parsed_url.path
    	response = urllib.urlopen(url)
    	data = response.read()
    	#Save the downloades file to the current directory
    	outfile_name = url.rpartition('/')[-1]
    	with open(outfile_name,'wb') as outfile:
    		outfile.write(data)
    	q.task_done()

# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
	worker = Thread(target=downloadEnclosures,args=(i,enclosure_queue,))
	worker.setDaemon(True)
	worker.start()

# Download the feed(s) and put the enclosure URLS into the queue
for url in feed_urls:
    response = feedparser.parse(url,agent='Queue_4.py')
for entry in response['entries'][-5:]:
    for enclosure in entry.get('enclosures',[]):
    	parsed_url = urlparse.urlparse(enclosure['link'])
    	print 'Queuing:',parsed_url.path
    	enclosure_queue.put(enclosure['link'])

#Now wait for the queue to be empty,indicating that we have processed all the downloades.
print '*** Main thread waiting'
enclosure_queue.join()
print '***Done'