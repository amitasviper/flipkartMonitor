import BeautifulSoup
import urllib2
from product import Product
from crawler import *
import os
import sys

def read_urls(filepath):
	with open(filepath, 'r') as url_file:
		return url_file.readlines()

def fetch_products_from_file():
	urls = read_urls(os.path.join(os.getcwd(),'urls.txt'))
	product_list = []
	for url in urls:
		product_name = url[24:].split('/')[0]
		product_list.append(Product(product_name, url))
	return product_list

def dummy_function():
	manager = Crawler()
	for pdt in fetch_products_from_file():
		manager.add_to_queue(pdt, QUEUE_URL)
	manager.start_execution()

class Flipkart(object):
	def __init__(self):
		self.product_list = fetch_products_from_file()


if __name__ == "__main__":
	dummy_function()