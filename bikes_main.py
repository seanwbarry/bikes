import bike_classes

bikes = {
	'Bike1': bike_classes.Bike('avanti', '1', 1000),
	'Bike2': bike_classes.Bike('avanti', '2', 2000),
	'Bike3': bike_classes.Bike('avanti', '3', 3000),
	'Bike4': bike_classes.Bike('avanti', '4', 4000),
	'Bike5': bike_classes.Bike('avanti', '5', 5000),
	'Bike6': bike_classes.Bike('avanti', '6', 6000)
}

customers = {
	'Customer1': bike_classes.Customers('a', 2000),
	'Customer2': bike_classes.Customers('b', 5000),
	'Customer3': bike_classes.Customers('c', 10000)	
}

inventory = {
	'Bike1': 2,
	'Bike2': 2,
	'Bike3': 2,
	'Bike4': 2,
	'Bike5': 2,
	'Bike6': 2
}



def what_can_customer_afford(customer):
#for customer in customers:
#	print(customer)
	for bike in bikes:
		if bikes[bike].cost<customers[customer].budget:
			print(bike)

def available_shop_inventory(bike):
	pass

def buy_a_bike(budget):
	pass

def which_bike_bought():
	pass

def how_much_money_left(budget):
	pass



