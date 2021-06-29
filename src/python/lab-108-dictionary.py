#
# filename   : lab-108-dictionary.py
# Description: Dictionary
# Docs       : - https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
#              - https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple
#

print('\n# 1. Dictionary\n')

d1 = { 'key#1': 'Value#1'}
print('type(d1) : ', type(d1))  # <class 'dict'>
d1['key#2'] = 'Value#2'
print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#2': 'Value#2'}


print('\n# 2. Dictionary - access by key\n')

print('d1[\'key#1\'] : ', d1['key#1'])  # 'Value#1'
print('d1[\'key#2\'] : ', d1['key#2'])  # 'Value#2'

try:
    print('d1[\'key-not-exists\'] : ', d1['key-not-exists'])  # KeyError: 'key-not-exists'
except:
    print('d1[\'key-not-exists\'] : KeyError: \'key-not-exists\'')


print('\n# 3. Dictionary - key are uniques\n')

d1['key#3'] = 'Value#3'
d1['key#3'] = 'Value#3.1'   # overwrite Value#3 with Value#3.1
d1['key#3'] = 'Value#3.2'   # overwrite Value#3.1 with Value#3.2
d1['key#3'] = 'Value#3.3'   # overwrite Value#3.2 with Value#3.3
print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#2': 'Value#2', 'key#3': 'Value#3.3'}


print('\n# 4. Dictionary - key datatypes alloweds: strings, numbers, tuples\n')

d2 = {
    'str': 'value#1',
    123: 'value#2',
    (1,2,3): 'value#3'
}
print('d2 : ', d2)                      # {'str': 'value#1', 123: 'value#2', (1, 2, 3): 'value#3'}
print('d2[(1,2,3)] : ', d2[(1,2,3)])    # value#3


print('\n# 5. Dictionary - test if a key exists\n')

if 'nao existe' in d2:
    print('existe')
else:
    print('nao existe com era esperado!')


print('d1.get(\'nao existe\')', d1.get('nao existe'))


print('\n# 6. Dictionary - update values\n')

print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#2': 'Value#2', 'key#3': 'Value#3.3'}
d1['key#3'] = 'NewValue#3'
print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#2': 'Value#2', 'key#3': 'NewValue#3'}
d1.update( {'key#3': 'UpdatedValue#3'} )  # another dictionary with a {key:value}
print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#2': 'Value#2', 'key#3': 'NewValue#3'}


print('\n# 7. Dictionary - delete {key: value} from dictionary\n')

del d1['key#2']
print('d1 : ', d1)  # {'key#1': 'Value#1', 'key#3': 'NewValue#3'}


print('\n# 8. Dictionary - listing keys, listing values\n')
print('d1.keys   : ', d1.keys)      # <built-in method keys of dict object at 0x000002BCE42FE1B0>
print('d1.values : ', d1.values())  # dict_values(['Value#1', 'UpdatedValue#3'])
print('len(d1)   : ', len(d1))      # 2

for key, value in d1.items():
    print(' - {', key, ': ', value, '}')    # { key#1 :  Value#1 }, { key#3 :  UpdatedValue#3 }


print('\n# 8. Dictionary - dictionary of dictionary\n')

clientes = {
    'cliente#1':
        {
            'name': 'Josemar',
            'sobrename': 'Silva'
        },
    'cliente#2':
        {
            'name': 'Maria',
            'sobrename': 'Silva'
        },
    'cliente#3':
        {
            'nome': 'Guilherme',
            'sobrenome': 'Silva'
        }
}

for key, value in clientes.items():
    print(f' + {key}')
    for subkey, subvalue in value.items():
        print(f'    - {subvalue}')

# + cliente#1
#    - Josemar
#    - Silva
# + cliente#2
#    - Maria
#    - Silva


print('\n# 9. Dictionary - alias vs copy\n')

d3 = {1: 'um', 2: 'dois', 3: 'tres'}
d4 = d3
print('d3 : ', d3)  # {1: 'um', 2: 'dois', 3: 'tres'}
print('d4 : ', d4)  # {1: 'um', 2: 'dois', 3: 'tres'}
d3[1] = 'one'
print('d3 : ', d3)  # {1: 'one', 2: 'dois', 3: 'tres'}
print('d4 : ', d4)  # {1: 'one', 2: 'dois', 3: 'tres'}

# both variables points to same position of memory

print('d3 == d4 : ', d3 == d4) # True

d5 = d4.copy()  # equivalente to CLONE variable in memory
d5[1] = 'um'
print('d4 == d5 : ', d4 == d5)  # False
print('d4 : ', d4)              # {1: 'one', 2: 'dois', 3: 'tres'}
print('d5 : ', d5)              # {1: 'um', 2: 'dois', 3: 'tres'}


print('\n# 10. Dictionary - concatenate two dictionaries\n')

d6 = {
    1: 'um',
    2: 'dois',
    3: 'tres',
}
d7 = {
    4: 'cuatro',
    5: 'cinco',
    6: 'ses',
    7: 'siete',
}
d8 = {
    8: 'eight',
    9: 'nine',
    10: 'ten'
}

try:
    d9 = d6 + d7 + d8 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
except:
    print('TypeError: unsupported operand type(s) for +: \'dict\' and \'dict\'')

d9 = d6.copy()
d9.update(d7)   # update dictionary keys from d7 into d9
d9.update(d8)   # update dictionary keys from d8 into d9
print('d6: ', d6)   # {1: 'um', 2: 'dois', 3: 'tres'}
print('d7: ', d7)   # {4: 'cuatro', 5: 'cinco', 6: 'ses', 7: 'siete', 8: 'eight', 9: 'nine', 10: 'ten'}
print('d8: ', d8)   # {8: 'eight', 9: 'nine', 10: 'ten'}

print('d9: ', d9)   # {1: 'um', 2: 'dois', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'ses', 7: 'siete', 8: 'eight', 9: 'nine', 10: 'ten'}
