#
# filename   : lab-120-reduce-lambda-function-as-parameter.py
# Description:
# Docs       : https://docs.python.org/3/library/importlib.html
#

print('\n1. Reduce Data\n')

import importlib
map_data = importlib.import_module("lab-117-map-data")
products = map_data.products
customers = map_data.customers
list_nums = map_data.list_nums

print(f'products : {products}')     # [{'name': 'product#1', 'price': 10.4}, {'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#4', 'price': 13.67}, {'name': 'product#5', 'price': 16.45}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}, {'name': 'product#9', 'price': 38.68}, {'name': 'product#10', 'price': 45.56}]
print(f'customers: {customers}')    # [{'name': 'Jose', 'age': 59}, {'name': 'Maria', 'age': 32}, {'name': 'Joao', 'age': 77}, {'name': 'Pedro', 'age': 41}, {'name': 'Paulo', 'age': 56}, {'name': 'Tiago', 'age': 31}, {'name': 'Isaias', 'age': 48}, {'name': 'Mateus', 'age': 65}, {'name': 'Andre', 'age': 61}, {'name': 'Tadeu', 'age': 52}]
print(f'list_nums: {list_nums}')    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('\n2. Reduce Data - Use reduce(lambda expression) - Reduce to sum of products price\n')

from functools import reduce

price_sum = reduce(lambda ac, p: p['price'] + ac, products, 0) # 0: initial value for ac
print(f'price_sum: {price_sum}')


print('\n3. Reduce Data - Use reduce(lambda expression) - Reduce to media of customers ages\n')

from functools import reduce

sum_age = reduce(lambda ac, c: c['age'] + ac, customers, 0) # 0: initial value for ac
print(f'sum_age: {sum_age}')
print(f'avg_age: {sum_age/len(customers)}')


