import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE players (name TEXT UNIQUE, level INT)')
print("Table created successfully")
conn.close()