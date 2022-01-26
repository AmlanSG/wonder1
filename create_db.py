import os
import sqlite3

db_filename = 'book'

db_exists = not os.path.exists(db_filename)
connection = sqlite3.connect(db_filename)
#db = sqlite3.connect('mydb')

if db_exists:
    print('No schema exists.')
else:
    print('DB exists.')
#db.close()
connection.close()