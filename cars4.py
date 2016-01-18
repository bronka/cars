import sqlite3

with sqlite3.connect("car.db") as cars:
	cursor = cars.cursor()

	cursor.execute("SELECT * FROM inventory WHERE Make = 'Ford'")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]

