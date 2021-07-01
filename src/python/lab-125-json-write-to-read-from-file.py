#
# filename   : lab-125-json-write-to-read-from-file.py
# Description: Json
# Docs       :  * https://docs.python.org/3.9/library/json.html?highlight=json#module-json
#               * https://docs.python.org/3.9/reference/import.html?highlight=import%20relative%20reference
#               * https://docs.python.org/3.9/reference/index.html
#

print('\n#1. Json \n')

import json
print(dir(json)) # ['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']


print('\n#2. Json - json.dumps(): Convert Dictionary to Json\n')

import json

# dictionary
d1 = {
    'Person #1': {
        'name': 'Jose',
        'age':  33
    },
    'Person #2': {
        'name': 'Maria',
        'age': 30
    },
    'Person #3': {
        'name': 'Pedro',
        'age': 50
    },
    'Person #3': {
        'name': 'Paulo',
        'age': 60
    },
}
json1= json.dumps(d1)

print(f'd1   : {d1}')       # {'Person #1': {'name': 'Jose', 'age': 33}, 'Person #2': {'name': 'Maria', 'age': 30}, 'Person #3': {'name': 'Paulo', 'age': 60}}
print(f'json1: {json1}')    # {"Person #1": {"name": "Jose", "age": 33}, "Person #2": {"name": "Maria", "age": 30}, "Person #3": {"name": "Paulo", "age": 60}}


print('\n#3. Json - Writting Json to file\n')

with open('file-01.json', 'w+') as file:
    file.write(json1)
    file.close()


print('\n#4. Json - Read Json from file\n')

with open('file-01.json', 'r') as file:
    str = file.read()
    file.close()

print(f'type(str): {type(str)}')    # <class 'str'>
print(f'str: {str}')    # {"Person #1": {"name": "Jose", "age": 33}, "Person #2": {"name": "Maria", "age": 30}, "Person #3": {"name": "Paulo", "age": 60}}


print('\n#5. Json - loads(): Convert Json to Dictionary\n')

with open('file-01.json', 'r') as file:
    str_dict_json = file.read()
    file.close()

print(f'type(str_dict_json): {type(str_dict_json)}')    # <class 'str'>
print(f'str_dict_json: {str_dict_json}')                # {"name": "Jose", "age": 33}, "Person #2": {"name": "Maria", "age": 30}, "Person #3": {"name": "Paulo", "age": 60}}
print('')
dict_json = json.loads(str_dict_json)
print(f'type(dict_json): {type(dict_json)}')    # <class 'dict'>
print(f'dict_json: {dict_json}')                # {'Person #1': {'name': 'Jose', 'age': 33}, 'Person #2': {'name': 'Maria', 'age': 30}, 'Person #3': {'name': 'Paulo', 'age': 60}}

for key, value in dict_json.items():
    print(f'- type(key), type(value): ( {type(key)},  {type(value)}) ')  # ( <class 'str'>,  <class 'dict'>)
    print(f'- key  : {key}')
    print(f'+ value: {value}')
    for key2, value2 in value.items():
        print(f'  - key2  : {key2}')
        print(f'  - value2: {value2}')

print('remove file: file-01.json')
import os
os.remove('file-01.json')
