#
# filename   : lab-114-iterable-zip-itertools-zip-longest.py
# Description: Iterable zip(), zip_longest(), count(), combinations()
# Docs       : * https://docs.python.org/3.9/library/itertools.html?highlight=zip#module-itertools
#

print('\n# 1. Iterable - zip()\n')

list_1a5 = [1, 2, 3, 4, 5]
list_1a5_portugues = ['um','dois','tres','quatro','cinco']
list_1a5_ingles = ['one', 'two','three','four','five']
list_1a5_espanhol = ['uno', 'dos', 'tres', 'cuatro','cinco']
list_1a5_frances = ['un', 'deux', 'trois', 'quatre', 'cinq']
list_1a5_alemao = ['eins', 'zwei', 'drei', 'vier', 'fünf']

z_list = zip(list_1a5, list_1a5_portugues, list_1a5_ingles, list_1a5_espanhol, list_1a5_frances, list_1a5_alemao)
print('z_list      : ', z_list)         # <zip object at 0x00000224C5CB8408>
print('list(z_list): ', list(z_list))   # [(1, 'um', 'one', 'uno', 'un', 'eins'), (2, 'dois', 'two', 'dos', 'deux', 'zwei'), (3, 'tres', 'three', 'tres', 'trois', 'drei'), (4, 'quatro', 'four', 'cuatro', 'quatre', 'vier'), (5, 'cinco', 'five', 'cinco', 'cinq', 'fünf')]


print('\n# 2. Iterable - zip_logest(), count()\n')

from itertools import zip_longest, count

list_1a10 = list(range(1,10+1))
print('list_1a10: ', list_1a10)
                    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z_list_with_none = zip_longest(list_1a10, list_1a5_portugues, list_1a5_ingles, list_1a5_espanhol, list_1a5_frances, list_1a5_alemao)
z_list_fill_null = zip_longest(list_1a10, list_1a5_portugues, list_1a5_ingles, list_1a5_espanhol, list_1a5_frances, list_1a5_alemao, fillvalue= 'null')
print('list(z_list_with_none): ', list(z_list_with_none))
                    # [(1, 'um', 'one', 'uno', 'un', 'eins'), (2, 'dois', 'two', 'dos', 'deux', 'zwei'), (3, 'tres', 'three', 'tres', 'trois', 'drei'), (4, 'quatro', 'four', 'cuatro', 'quatre', 'vier'), (5, 'cinco', 'five', 'cinco', 'cinq', 'fünf'), (6, None, None, None, None, None), (7, None, None, None, None, None), (8, None, None, None, None, None), (9, None, None, None, None, None), (10, None, None, None, None, None)]
print('list(z_list_fill_null): ', list(z_list_fill_null))
                    # [(1, 'um', 'one', 'uno', 'un', 'eins'), (2, 'dois', 'two', 'dos', 'deux', 'zwei'), (3, 'tres', 'three', 'tres', 'trois', 'drei'), (4, 'quatro', 'four', 'cuatro', 'quatre', 'vier'), (5, 'cinco', 'five', 'cinco', 'cinq', 'fünf'), (6, 'null', 'null', 'null', 'null', 'null'), (7, 'null', 'null', 'null', 'null', 'null'), (8, 'null', 'null', 'null', 'null', 'null'), (9, 'null', 'null', 'null', 'null', 'null'), (10, 'null', 'null', 'null', 'null', 'null')]

count_index = count()
z_list_count_index = zip(
    count_index,
    list_1a5_portugues,
    list_1a5_ingles,
    list_1a5_espanhol,
    list_1a5_frances,
    list_1a5_alemao
)
print('list(z_list_count_index): ', list(z_list_count_index))
                    # [(0, 'um', 'one', 'uno', 'un', 'eins'), (1, 'dois', 'two', 'dos', 'deux', 'zwei'), (2, 'tres', 'three', 'tres', 'trois', 'drei'), (3, 'quatro', 'four', 'cuatro', 'quatre', 'vier'), (4, 'cinco', 'five', 'cinco', 'cinq', 'fünf')]
print('count_index: ', count_index)                 # 6
print('count_index: ', count_index)                 # 6
next(count_index)
print('count_index: ', count_index)                 # 7


print('\n# 3. Iterable - unpacking zip\n')
z_list = zip(list_1a5, list_1a5_portugues, list_1a5_ingles, list_1a5_espanhol, list_1a5_frances, list_1a5_alemao)
print('list(z_list): ', list(z_list))  # [(1, 'um', 'one', 'uno', 'un', 'eins'), (2, 'dois', 'two', 'dos', 'deux', 'zwei'), (3, 'tres', 'three', 'tres', 'trois', 'drei'), (4, 'quatro', 'four', 'cuatro', 'quatre', 'vier'), (5, 'cinco', 'five', 'cinco', 'cinq', 'fünf')]
print(type(z_list))     # <class 'zip'>


print('\n# 3. Iterable - count is iterator not a generator\n')

from itertools import count
from types import GeneratorType
variable = (zip('um', 'dois', 'tres'))
print('isinstance(variable, GeneratorType): ', isinstance(variable, GeneratorType))

infinito = count(start=1,step=0.5)  # count() é um iterador infinito
for i in infinito:
    print(f'i: {i}')
    if i > 100:
        break   # saindo do loop infinito


infinito = count(start=100,step=-0.5)  # count() é um iterador infinito
for i in infinito:
    print(f'i: {i}')
    if i < 0:
        break   # saindo do loop infinito


print('\n# 5. Iterable - count is iterator not a generator\n')

from itertools import count
contador = count()
l1 = [ 'Jose', 'Maria', 'Joao', 'Pedro', 'Matheus']
l2 = zip(contador,l1)
print('l1      : ', l1)         # ['Jose', 'Maria', 'Joao', 'Pedro', 'Matheus']
print('l2      : ', l2)         # <zip object at 0x0000013DB3ECE2C8>
print('list(l2): ', list(l2))   # [(0, 'Jose'), (1, 'Maria'), (2, 'Joao'), (3, 'Pedro'), (4, 'Matheus')]

for i, v in l2:
    print(i, v)     # nao entendi porque nao pega
for r in l2:
    print(r)        # nao entendi porque nao pega
for r in list(l2):
    print(r)        # nao entendi porque nao pega
