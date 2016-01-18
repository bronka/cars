import sqlite3

with sqlite3.connect("car.db") as cars:

	cursor = cars.cursor()

	cursor.execute("INSERT INTO inventory VALUES('Ford', 'A', 22)")
	cursor.execute("INSERT INTO inventory VALUES('Ford', 'B', 30)")
	cursor.execute("INSERT INTO inventory VALUES('Ford', 'Blaa', 2)")
	cursor.execute("INSERT INTO inventory VALUES('Honda', 'Fruu', 122)")
	cursor.execute("INSERT INTO inventory VALUES('Honda', 'Blee', 345)")