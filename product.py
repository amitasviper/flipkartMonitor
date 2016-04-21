class Product(object):
	def __init__(self, name, url):
		self.name = name
		self.url = url
		self.price = 0.0
		self.old_price = 0.0
		self.new_price = -1.0
		self.min_price = 0.0
		self.max_price = 0.0
		self.discount_percent = 0.0
		self.monitor = True

	def update_url(self, new_url):
		self.url = new_url
		#Add an api to update the url in the databse as well

	def update_price(self, new_price):
		self.old_price = self.price
		self.price = new_price
		#Add an api to update the price in the databse as well
		#add a watchdog here

	def calculate_discount(self):
		#add api to calculate the discount offered on the product
		pass

	def update_monitor_status(self, value):
		self.monitor = value