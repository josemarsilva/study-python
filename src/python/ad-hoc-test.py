#
# filename   : ad-hoc-test.py
# Description:
# Docs       :
# Requirements:
#               * pip install requirements
#               * pip install plotly --upgrade
#


import requests
r=requests.get("https://raw.githubusercontent.com/josemarsilva/study-python/main/src/python/file-06-trecho-livro-filosofia.txt")
print(r.text)

with open('file-01-csv-utf7.csv', 'r') as file:
    print(file.readlines())