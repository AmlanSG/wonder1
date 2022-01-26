import sqlite3

db_filename = 'journaldev.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, name, day_effort, book from chapter
    where book = 'JournalDev'
    """)

    for row in cursor.fetchall():
        id, name, day_effort, book = row
        print('{:2d} ({}) {:2d} ({})'.format(
            id, name, day_effort, book))