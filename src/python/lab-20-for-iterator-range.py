#
# filename   : lab-20-for-iterator-range.py
# Description: For iterator, range,
# Docs       : https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
#

print('\n# 1. For iterator, range() \n')

#        0         1         2         3
#        0123456789012345678901234567890123456789

print(f'Range de 10 elementos - (0 .. 9)')
for n in range(10):
    print(f'{n}')           # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print('')
print(f'Range de 10 elementos - (1 .. 10)')
for n in range(1,10+1):
    print(f'{n}')           # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print('')
print(f'Range de 10 elementos, início em 1, saltos de 2  - (1 .. 10)')
for n in range(1,10,2):
    print(f'{n}')           # 1, 3, 5, 7, 9


frase = 'O rato roeu a roupa do rei de roma'
nova_frase = ''
for letra in frase:
    if letra == ' ':
        continue
    else:
        nova_frase = nova_frase + letra

print(f'nova frase: {nova_frase}')