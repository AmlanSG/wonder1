import sqlite3

db_filename = 'journaldev.db'

def show_books(conn):
    cursor = conn.cursor()
    cursor.execute('select name, topic from book')
    for name, topic in cursor.fetchall():
        print('  ', name)


with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    show_books(conn1)

    # Insert in one cursor
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into book (name, topic, published)
    values ('Welcome Python', 'Python', '2013-01-01')
    """)

    print('\nAfter changes in conn1:')
    show_books(conn1)

    # Select from another connection, without committing first
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        show_books(conn2)

    # Commit then select from another connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        show_books(conn3)