import Queue
from threading import Thread
import BeautifulSoup as bs
import urllib2
import time
import os
import sys
from product import Product
from dataminingworker import *
from urlworker import *

QUEUE_URL = 1
QUEUE_RESULT = 2

class Crawler(object):
	def __init__(self, thread_count=4):
		self.thread_count = thread_count
		self.url_queue = Queue.Queue()
		self.result_queue = Queue.Queue()
		self.url_workers = []

	def start_execution(self):
		worker = Worker(self.url_queue, self.result_queue)
		datamining = DataMiningWorker(self.result_queue)
		worker.start()
		datamining.start()


	def add_to_queue(self, data, queue_name):
		if queue_name == QUEUE_URL:
			self.url_queue.put(data)
		elif queue_name == QUEUE_RESULT:
			self.result_queue.put(data)
		else:
			print "Invalid queue identifier"