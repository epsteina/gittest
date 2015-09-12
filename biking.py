class Bicycle(object):
	def __init__(self, name, weight, prodcost, shop, stock):
		self.weight = weight
		self.prodcost = prodcost
		self.name = name
		self.shop = shop
		self.stock = stock
		for store in stores:
			if store.name == self.shop:
				store.inventory.append(self)

class Bike_Shop(object):
	def __init__(self, markup, name,inventory):
		self.markup = markup
		self.name = name
		self.inventory = inventory

	def listinventory(self):
			for bike in self.inventory:
				print bike.name  + " (" + str(bike.stock) + " in stock)"

	def custopt(self,cust):
		options = []
		print "Customer name: " + cust.name
		print "Budget: " + str(cust.funds)
		print cust.name + " can afford the following models:"
		for model in self.inventory:
			if model.prodcost * (1 + self.markup) <= cust.funds:
				if model.stock == 0:
					print model.name + " (out of stock)"
				else:
					print model.name
					options.append(model)
		return options

class Customer(object):
	def __init__(self, name, funds, options):
		self.funds = funds
		self.name = name
		self.options = options

	def purchase(self,store):
		cost = self.options[0].prodcost * (1+store.markup)
		self.funds = self.funds-cost
		print self.name + " purchases " + self.options[0].name + " for $" + str(cost),
		print " and has $" + str(self.funds) + " left"
		self.options[0].stock -= 1



Customer1 = Customer("John",200, [])
Customer2 = Customer("Mike",500, [])
Customer3 = Customer("Susan",1000, [])

ABC_Bikes = Bike_Shop(0.2, "ABC Bikes",[])

stores = [ABC_Bikes]
customers = [Customer1, Customer2, Customer3]

ModelA = Bicycle("Model A", 25,450, "ABC Bikes",8)
ModelB = Bicycle("Model B", 35,399, "ABC Bikes",9)
ModelC = Bicycle("Model C", 20,550, "ABC Bikes",0)
ModelD = Bicycle("Model D", 15,900, "ABC Bikes",3)
ModelE = Bicycle("Model E", 30,350, "ABC Bikes",6)
ModelF = Bicycle("Model F", 30,150, "ABC Bikes",2)

print "Initial Inventory"
ABC_Bikes.listinventory()

for cust in customers:
	cust.options = ABC_Bikes.custopt(cust)
	cust.purchase(ABC_Bikes)

print "Final Inventory"
ABC_Bikes.listinventory()
