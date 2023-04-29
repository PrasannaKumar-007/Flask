import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE users (fname TEXT, lname TEXT, email TEXT, password TEXT, pin TEXT)')

conn.close()
