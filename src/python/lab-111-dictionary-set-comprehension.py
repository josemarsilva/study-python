#
# filename   : lab-111-dictionary-set-comprehension.py
# Description: Dictionary
# Docs       : - https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#              - https://docs.python.org/3/tutorial/datastructures.html#sets
#

print('\n# 1. Dictionary and Set Comprehension\n')

print('\n# 2. List of tuples into Dictionary\n')

# list of tuple (chave, valor)
l1 = [
    ('key#1', 'value#1'),
    ('key#2', 'value#2'),
    ('key#3', 'value#3')
]
# dictionary
d1 = dict(l1)
d2 = {x: y for x,y in l1}
d3 = {x: y.upper() for x,y in l1}


print('l1: ', l1)   # [('key#1', 'value#1'), ('key#2', 'value#2'), ('key#3', 'value#3')]
print('d1: ', d1)   # {'key#1': 'value#1', 'key#2': 'value#2', 'key#3': 'value#3'}
print('d2: ', d2)   # {'key#1': 'value#1', 'key#2': 'value#2', 'key#3': 'value#3'}
print('d3: ', d3)   # {'key#1': 'VALUE#1', 'key#2': 'VALUE#2', 'key#3': 'VALUE#3'}


print('\n# 3. Range enumerated into Dictionary\n')
d1 = {x: y for x, y in enumerate(range(5)) }  # range(5): [0,1,2,3,4]
print('d1: ', d1)   #  {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

d2 = {x for x in range(5) }     # range(5): [0,1,2,3,4]
                                # Atenção: d2 é um SET nao um dictionary
print('d2      : ', d2)         # {0, 1, 2, 3, 4}
print('type(d2): ', type(d2))   # <class 'set'>

d3 = {f'key#{x}': x**2 for x in range(5) }   # range(5): [0,1,2,3,4]
print('d3: ', d3)  # {'key#0': 0, 'key#1': 1, 'key#2': 4, 'key#3': 9, 'key#4': 16}
