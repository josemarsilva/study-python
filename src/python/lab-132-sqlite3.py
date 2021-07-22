#
# filename    : lab-132-sqlite3.py
# Description : SQLite3 database connection with sqlite3
# Docs        :
#               * https://pypi.org/project/pyodbc/
# Requirements:
#               * pip install pyodbc
#

import sqlite3

# connect() cursor()
conn = sqlite3.connect('sqlite3_database.db')
cursor = conn.cursor()

# execute create tables ...
cursor.execute('DROP TABLE IF EXISTS customers' )
cursor.execute('CREATE TABLE IF NOT EXISTS customers ( '
               'id INTEGER PRIMARY KEY AUTOINCREMENT, '
               'name TEXT, '
               'age INTEGER,'
               'salary REAL'
               ')'
               )

# insert - sql injection
cursor.execute('INSERT INTO customers (name, age, salary) VALUES ("Josemar Silva", 52, 1234567.89)')
conn.commit()

# insert - binding with question mark
cursor.execute('INSERT INTO customers (name, age, salary) VALUES (?, ?, ?)',
               ('Maria  Silva', 48, 987.56)
)
conn.commit()

# insert - binding with dictionary
cursor.execute('INSERT INTO customers (name, age, salary) VALUES (:name, :age, :salary)',
               {'name': 'Guilherme Silva', 'age': 28, 'salary': 43.21}
)
#conn.commit()

# insert - binding with dictionary
cursor.execute('INSERT INTO customers (name, age, salary) VALUES (:name, :age, :salary)',
               {'name': 'Gabrielle Silva', 'age': 20, 'salary': 123.45}
)
#conn.commit()

# insert - binding with dictionary
cursor.execute('INSERT INTO customers (name, age, salary) VALUES (:name, :age, :salary)',
               {'name': 'Melani Shitzu', 'age': 10, 'salary': 0.00}
)
#conn.commit()

# update - binding dictionary
cursor.execute('UPDATE customers SET name=:name, age=:age, salary=:salary WHERE id=:id',
               {'name': 'Maria Stela Silva', 'age': 28, 'salary': 43.21, 'id': 2}
)
#conn.commit()

# delete - binding dictionary
cursor.execute('DELETE FROM customers WHERE name=:name',
               {'name': 'Melani Shitzu'}
)
#conn.commit()

# select
cursor.execute('SELECT * FROM customers')
for result_set in cursor.fetchall():
    identity, name, age, salary = result_set
    print(identity, name, age, salary)
#

# close() ...
cursor.close()
conn.close()
