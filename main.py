import sqlite3

with sqlite3.connect('db/test.db') as conn:
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE test (id INTEGER PRIMARY KEY AUTOINCREMENT, test TEXT ) ''')
    conn.commit() 