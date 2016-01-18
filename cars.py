import sqlite3

cars = sqlite3.connect("car.db")

cursor = cars.cursor()

cursor.execute("""CREATE TABLE inventory (Make TEXT, Model TEXT, Quantity INT)""")

cars.close()