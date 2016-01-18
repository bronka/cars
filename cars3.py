import sqlite3

with sqlite3.connect("car.db") as cars:
	cursor = cars.cursor()

	cursor.execute("UPDATE inventory SET Quantity = 50 WHERE Model = 'A'")
	cursor.execute("UPDATE inventory SET Quantity = 100 WHERE Model = 'Blaa'")

	print "\nNEW DATA: \n" 

	cursor.execute("SELECT * FROM inventory")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]