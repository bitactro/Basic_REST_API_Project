import sqlite3

conn = sqlite3.connect("bookdb.db")

conn.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title text, desc text, price integer)")

conn.close()