#
# filename   : lab-118-map-lambda-function-as-parameter.py
# Description:
# Docs       : https://docs.python.org/3/library/importlib.html
#

print('\n1. Map Data\n')

import importlib
map_data = importlib.import_module("lab-117-map-data")
products = map_data.products
customers = map_data.customers
list_nums = map_data.list_nums

print(f'products : {products}')     # [{'name': 'product#1', 'price': 10.4}, {'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#4', 'price': 13.67}, {'name': 'product#5', 'price': 16.45}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}, {'name': 'product#9', 'price': 38.68}, {'name': 'product#10', 'price': 45.56}]
print(f'customers: {customers}')    # [{'name': 'Jose', 'age': 59}, {'name': 'Maria', 'age': 32}, {'name': 'Joao', 'age': 77}, {'name': 'Pedro', 'age': 41}, {'name': 'Paulo', 'age': 56}, {'name': 'Tiago', 'age': 31}, {'name': 'Isaias', 'age': 48}, {'name': 'Mateus', 'age': 65}, {'name': 'Andre', 'age': 61}, {'name': 'Tadeu', 'age': 52}]
print(f'list_nums: {list_nums}')    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('\n2. Multiply all list elements x2 - use  map\n')

map_nums_double = map(lambda x: x*2, list_nums)
print(f'map_nums_double      : {map_nums_double}')
print(f'type(map_nums_double): {type(map_nums_double)}')
print(f'list(map_nums_double): {list(map_nums_double)}')  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print('\n3. Multiply all list elements x2 - use iterator\n')

list_nums_double = [x * 2 for x in list_nums]
print(f'list_nums_double: {list_nums_double}') # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print('\n3. Multiply all dictionary prices x2 - use map\n')

print('products : ', products) # [{'name': 'product#1', 'price': 10.4}, {'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#4', 'price': 13.67}, {'name': 'product#5', 'price': 16.45}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}, {'name': 'product#9', 'price': 38.68}, {'name': 'product#10', 'price': 45.56}]
for product in products:
    print(f'product: {product}')

prices = map(lambda p: p['price'] * 2, products)
print(f'list(prices): {list(prices)}')  # [20.8, 160.8, 101.6, 27.34, 32.9, 196.4, 183.7, 144.6, 77.36, 91.12]


print('\n4. Multiply all dictionary prices x2 - use  function\n')

def multiply_price_by(p):
    factor = 2
    p['price'] = round(p['price'] * factor, 2)
    return p

print('products : ', products) # [{'name': 'product#1', 'price': 10.4}, {'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#4', 'price': 13.67}, {'name': 'product#5', 'price': 16.45}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}, {'name': 'product#9', 'price': 38.68}, {'name': 'product#10', 'price': 45.56}]
map_new_products = map(multiply_price_by, products)
print(f'type(map_new_products): {type(map_new_products)}')  #  <class 'map'>
print(f'list(map_new_products): {list(map_new_products)}')  # [{'name': 'product#1', 'price': 15.6}, {'name': 'product#2', 'price': 120.6}, {'name': 'product#3', 'price': 76.2}, {'name': 'product#4', 'price': 20.5}, {'name': 'product#5', 'price': 24.67}, {'name': 'product#6', 'price': 147.3}, {'name': 'product#7', 'price': 137.77}, {'name': 'product#8', 'price': 108.45}, {'name': 'product#9', 'price': 58.02}, {'name': 'product#10', 'price': 68.34}]


print('\n5. List only customers names from dictionary\n')

customer_names = map(lambda cn: cn['name'], customers)
print(f'customer_names: {customer_names}')       # <map object at 0x0000019FEE758E10>
print(f'customer_names: {list(customer_names)}') # customer_names: ['Jose', 'Maria', 'Joao', 'Pedro', 'Paulo', 'Tiago', 'Isaias', 'Mateus', 'Andre', 'Tadeu']


print('\n5. Increment customers age from dictionary - use lambda and function as parameter\n')

def increment_age(c):
    age_increment = 1
    c['new_age'] = c['age'] + age_increment
    return c

print(f'customers: {customers}')
map_new_customers = map(increment_age, customers)
print(f'type(map_new_customers): {type(map_new_customers)}')  #  <class 'map'>
print(f'list(map_new_customers): {list(map_new_customers)}')  #  [{'name': 'Jose', 'age': 59, 'new_age': 60}, {'name': 'Maria', 'age': 32, 'new_age': 33}, {'name': 'Joao', 'age': 77, 'new_age': 78}, {'name': 'Pedro', 'age': 41, 'new_age': 42}, {'name': 'Paulo', 'age': 56, 'new_age': 57}, {'name': 'Tiago', 'age': 31, 'new_age': 32}, {'name': 'Isaias', 'age': 48, 'new_age': 49}, {'name': 'Mateus', 'age': 65, 'new_age': 66}, {'name': 'Andre', 'age': 61, 'new_age': 62}, {'name': 'Tadeu', 'age': 52, 'new_age': 53}]

