#
# filename   : aula-103-def-return-list-tuple.py
# Description: functions returns
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#

print('\n# 1. Function return list\n')

def cores_primarias():
    return ['amarelo', 'azul', 'vermelho']


print('cores_primarias        : ', cores_primarias)         # <function cores_primarias at 0x0000017EC31DFE18>
print('cores_primarias()      : ', cores_primarias())       # ['amarelo', 'azul', 'vermelho']
print('type(cores_primarias()): ', type(cores_primarias())) # <class 'list'>

print('\n# 2. Function return tuple\n')

def tuple():
    return ('key', 'value')

print('tuple()      : ', tuple())        # ('key', 'value')
print('type(tuple()): ', type(tuple()))  # <class 'tuple'>
