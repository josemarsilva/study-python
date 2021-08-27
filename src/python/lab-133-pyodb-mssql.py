#
# filename    : lab-133-pyodb-sqlserver.py
# Description : SQLServer database connection with pyodbc
# Docs        :
#               * https://pypi.org/project/pymssql/
# Requirements:
#               * pip install pymssql
#

import pymssql

# #############################################################################

# connect() cursor()
server = 'localhost'
user = 'northwind_user'
password = 'northwind_user'
database = 'northwind'
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()

# select - fetch all
cursor.execute('SELECT * FROM Categories')
for row in cursor.fetchall():
    print(row[0], row[1], row[2])
#

# select - fetch one
print('')
cursor.execute('SELECT TOP 10 * FROM Customers')
row = cursor.fetchone()
print(row)

# cursor.close(), connection.close() ...
cursor.close()
conn.close()

# #############################################################################

with pymssql.connect(server, user, password, database) as conn:
    with conn.cursor(as_dict=True) as cursor:  # nao gostei do as_dict
        cursor.execute('SELECT TOP 10 * FROM Customers')
        for row in cursor:
            print(row['CustomerID'], ';',  row['CompanyName'], ';',  row['ContactName'])  # usar como dict e não como array[int]
        #
        cursor.execute('SELECT COUNT(*) AS Count FROM Customers')
        row = cursor.fetchone()
        print('COUNT(*): ', row['Count']) # COUNT(*):  91

        # SELECT NO_DATA_FOUND
        cursor.execute('SELECT CustomerId FROM Customers WHERE CompanyName = %s', 'not exist')
        row = cursor.fetchone()
        print('row: ', row) # None

# #############################################################################
