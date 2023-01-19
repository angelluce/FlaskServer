import sqlite3

connection = sqlite3.connect('db/database.db')


with open('db/script.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Hola mundo', 'Contenido del post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Python, Flask', 'Contenido del post')
            )

connection.commit()
connection.close()