#
# filename    : file-16-includable-config-file.py
# Description : Config file included by another Python program
# Docs        :
#               * https://martin-thoma.com/configuration-files-in-python/
# Requirements:
#               * n/a

mysql = {
    # {key,value}
    "host": "localhost",
    "user": "root",
    "password": "password123",
    "dbname": "mydb",
    # tuple indexing key
    ("dbname", "tablename"): "mytable",
    ("dbname", "tablename", "id_column"): "id",
    ("dbname", "tablename", "name_column"): "name",
    # values are list
    "tablenames":[
        "othertable1",
        "othertable2"
    ],
    # values are another dictionary
    "tables":{
        "mytable1": ["id", "name"],
        "mytable2": ["id", "name"]
    }
}