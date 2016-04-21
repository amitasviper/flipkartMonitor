import Queue
from threading import Thread
import time
from BeautifulSoup import BeautifulSoup
from product import Product

class DataMiningWorker(Thread):
	def __init__(self, queue_pdct_src):
		Thread.__init__(self)
		self.queue_pdct_src = queue_pdct_src

	def extract_price(self, soup):
		span_class = "selling-price omniture-field"
		value_string = "data-evar48"
		price_list = []
		for span in soup.findAll("span", {"class" : span_class}):
			#print span
			price_list.append(span[value_string])
		return price_list

	def process_details(self, details):
		print "DataMiningWorker Thread : Details : ", details

	def run(self):
		while True:
			#get product info and page source from the queue
			product_info, src = self.queue_pdct_src.get()
			print "DataMiningWorker: got data to process"

			#Parse the source code
			soup = BeautifulSoup(src)
			details = self.extract_price(soup)

			#Process the details extracted from the source code
			self.process_details(details)

			#signal to the queue that job is done
			self.queue_pdct_src.task_done()