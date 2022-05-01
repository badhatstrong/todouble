import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()

cur.execute('''CREATE TABLE notes
                (id integer primary key, note text)''')
con.commit()
con.close()
