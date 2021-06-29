#
# filename   : lab-115-itertools-combinations-permutations-products.py
# Description: Iterable zip(), zip_longest(), count(), combinations()
# Docs       : * https://docs.python.org/3.9/library/itertools.html?highlight=zip#module-itertools
#

print('\n# 1. Iterable - combinations() permutations() product() \n')

from itertools import combinations, permutations, product

l1 = [1, 2, 3, 4, 5]
l2 = [ False, True]
l3 = ['a', 'e', 'i', 'o', 'u']
l4 = ['amarelo', 'azul', 'vermelho']

print('+ combinations(l1,2): Sort is not important')
for list_combinations in combinations(l1,2):
    print(f'  - list_combinations: {list_combinations}')

print('+ permutations(l1,2): Sort is important but do not repeat values')
for list_permutations in permutations(l1,2):
    print(f'  - list_permutations: {list_permutations}')


print('+ product(l1,repeat=2): Sort is important and repeated values are considerated')
for list_product in product(l1,repeat=2):
    print(f'  - list_product: {list_product}')
