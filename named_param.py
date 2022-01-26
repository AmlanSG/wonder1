import sqlite3
import sys

db_filename = 'journaldev.db'
book_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, name, day_effort, book from chapter
    where book = :book_name
    """

    cursor.execute(query, {'book_name': book_name})
    for row in cursor.fetchall():
        id, name, day_effort, book = row
        print('{:2d} ({}) {:2d} ({})'.format(
            id, name, day_effort, book))