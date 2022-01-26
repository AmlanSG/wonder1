import os
import sqlite3

db_filename = 'book'
schema_filename = 'book_schema.sql'

db_exists = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_exists:
        print('Creating schema')
        with open(schema_filename, 'rt') as file:
            schema = file.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""
        insert into book (name, topic, published)
        values ('JournalDev', 'Java', '2011-01-01');

        insert into chapter (name, day_effort, book)
        values ('Java XML', 2,'JournalDev');

        insert into chapter (name, day_effort, book)
        values ('Java Generics', 1, 'JournalDev');

        insert into chapter (name, day_effort, book)
        values ('Java Reflection', 3, 'JournalDev');
        """)
        print('DB Created Schema Created Data inserted')
    else:
        print('DB already exists.')
        
        conn.close()