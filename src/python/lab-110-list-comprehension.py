#
# filename   : lab-110-list-comprehension.py
# Description: Dictionary
# Docs       : https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#

print('\n# 1. List Comprehension\n')


print('\n# 2. Iterate each list element\n')

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [var for var in l1]
l3 = l1
l3.append(10)
                                # Pegadinhas:
                                # l3 = l1 criou um 'alias' para a mesma posicao de memoria
                                # uma alteração em l3 também alterou l1
                                # l2 tirou uma cópia de l1 antes da modificação
print('l1      : ', l1)         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('l2      : ', l2)         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('l3      : ', l3)         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('l1 == l2: ', l1 == l2)   # False - Porque l2 tirou uma copia antes da modificação
print('l1 == l3: ', l1 == l3)   # True - Porque a atribuição 'l3 = l1' fez l3 apontar para o
                                #        mesmo endereco de memoria que armazena os dados de l1


print('\n# 3. Iterate each list element - apply mathematic operation\n')

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [var * 2 for var in l1]
print('l1      : ', l1)         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('l2      : ', l2)         # [2, 4, 6, 8, 10, 12, 14, 16, 18]


print('\n# 4. Iterate each list element - create tuple with elements\n')

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(3): [0, 1, 2]
l2 = [(var1, var2)  for var1 in l1 for var2 in range(3)]
print('l1      : ', l1)         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('l2      : ', l2)         # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]


print('\n# 5. Iterate each list element - apply function over each element\n')

l1 = ['Jose', 'Maria', 'Joao', 'Pedro', 'Matheus']
l2 = [v.replace('a','@').replace('e','3').replace('i','1').replace('o','0').replace('u','11') for v in l1]
print('l1      : ', l1)         # ['Jose', 'Maria', 'Joao', 'Pedro', 'Matheus']
print('l2      : ', l2)         # ['J0s3', 'M@r1@', 'J0@0', 'P3dr0', 'M@th311s']


print('\n# 5. Iterate each list element - invert position of elements\n')

tupla = (
    ('chave#1', 'valor#1'),
    ('chave#2', 'valor#2'),
    ('chave#3', 'valor#3'),
    ('chave#4', 'valor#4'),
    ('chave#5', 'valor#5')
)

tupla_invertida = [(y,x) for x, y in tupla]
dict_invertido = dict(tupla_invertida)
print('tupla          : ', tupla)           # (('chave#1', 'valor#1'), ('chave#2', 'valor#2'), ('chave#3', 'valor#3'), ('chave#4', 'valor#4'), ('chave#5', 'valor#5'))
print('tupla_invertida:', tupla_invertida)  # [('valor#1', 'chave#1'), ('valor#2', 'chave#2'), ('valor#3', 'chave#3'), ('valor#4', 'chave#4'), ('valor#5', 'chave#5')]
print('dict_invertido :', dict_invertido)   # {'valor#1': 'chave#1', 'valor#2': 'chave#2', 'valor#3': 'chave#3', 'valor#4': 'chave#4', 'valor#5': 'chave#5'}


print('\n# 6. Iterate each list element - apply function to each element\n')

l1 = list(range(100))                               # range(100) = [1, 2, ..., 99]
l2 = [v for v in l1 if v % 2 == 0]                  # each element divisible by 2
l3 = [v for v in l1 if v % 2 == 0 if v % 3 == 0 ]   # each element divisible by 2 and by 3
l4 = [v if v % 2 == 0 else 'impar' for v in l1 ]    # each odd element
print('l1: ', l1)   # [0, 1, 2, 3, ... , 99]
print('l2: ', l2)   # [0, 2, 4, 6, ... , 98]
print('l3: ', l3)   # [0, 6, 12, ... 90, 96]
print('l4: ', l4)   # [0, 'impar', 2, 'impar', 4, 'impar', .. , 98, 'impar']


print('\n# 7. Iterate each list element - apply complex expression\n')

from math import pi
l1 = [str(round(pi, i)) for i in range(1, 8)]   # pi values with n decimal places
print('l1: ', l1)   # ['3.1', '3.14', '3.142', '3.1416', '3.14159', '3.141593', '3.1415927']


print('\n# 8. Iterate nested list - matrix, transpose matrix\n')

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]
matrix_transpose = [[row[i] for row in matrix] for i in range(4)]
print('matrix          : ', matrix)             # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print('matrix_transpose: ', matrix_transpose)   # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]