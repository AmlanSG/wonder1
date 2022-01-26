import sqlite3

db_filename = 'journaldev.db'

with sqlite3.connect(db_filename) as connection:
    cursor = connection.cursor()

    cursor.execute("""
    select * from chapter where book = 'JournalDev'
    """)

    print('Chapter table has these columns:')
    for column_info in cursor.description:
        print(column_info)