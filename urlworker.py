import Queue
from threading import Thread
import urllib2
import time
from product import Product

class Worker(Thread):
	def __init__(self, queue_task, queue_result):
		Thread.__init__(self)
		self.queue_task = queue_task
		self.queue_result = queue_result


	def run(self):
		while True:
			#extract a product from the queue, if it exists
			product_info = self.queue_task.get()
			print "Worker : got data to process"

			page_source = urllib2.urlopen(product_info.url)
			self.queue_result.put((product_info, page_source))

			#signal the input queue that task is done
			self.queue_task.task_done()


