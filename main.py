import sqlite3

with sqlite3.connect('db/test.db') as conn:
    cursor = conn.cursor()
    cursor.execute(''' INSERT INTO test (test) VALUES ('test') ''')
    conn.commit() 