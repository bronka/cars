import sqlite3

with sqlite3.connect("car.db") as cars:
	cursor = cars.cursor()

	cursor.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_data TEXT)""")

	order = [
				('Ford', 'A', '1999-10-22'),
				('Ford', 'A', '2005-11-11'),
				('Ford', 'A', '1998-12-17'),
				('Ford', 'B', '2000-03-12'),
				('Ford', 'B', '2008-01-19'),
				('Ford', 'B', '1996-09-29'),
				('Ford', 'Blaa', '2009-06-01'),
				('Ford', 'Blaa', '2000-03-17'),
				('Ford', 'Blaa', '2010-08-09'),
				('Ford', 'Blaa', '2004-10-04'),
				('Honda', 'Fruu', '2003-04-05'),
				('Honda', 'Fruu', '2006-12-12'),
				('Honda', 'Fruu', '2001-10-04'),
				('Honda', 'Blee', '2001-07-16'),
				('Honda', 'Blee', '1995-02-02'),
				('Honda', 'Blee', '2014-03-03')
			]

	cursor.executemany("INSERT INTO orders VALUES(?, ?, ?)", order)

	cursor.execute("""SELECT DISTINCT inventory.make, inventory.model, 
				inventory.quantity, orders.order_data FROM inventory, orders WHERE 
				inventory.Make = orders.make and inventory.Model = orders.model ORDER BY
				inventory.make ASC""")

	rows = cursor.fetchall()

	for r in rows:
		print "Make: " + r[0] + " Model: " + r[1]
		print "Quantity: " + str(r[2])
		print "Order dates: " + r[3]
		print