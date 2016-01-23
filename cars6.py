import sqlite3

with sqlite3.connect("car.db") as cars:
	cursor = cars.cursor()

	cursor.execute("SELECT Make, Model, Quantity, (select count(orders.order_data) from orders where orders.model=inventory.Model ) from inventory")

	row = cursor.fetchall()

	for r in row:
		print r[0], r[1]
		print r[2]
		print r[3]

