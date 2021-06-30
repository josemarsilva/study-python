#
# filename   : lab-119-filter-lambda-function-as-parameter.py
# Description:
# Docs       : https://docs.python.org/3/library/importlib.html
#

print('\n1. Filter Data\n')

import importlib
map_data = importlib.import_module("lab-117-map-data")
products = map_data.products
customers = map_data.customers
list_nums = map_data.list_nums

print(f'products : {products}')     # [{'name': 'product#1', 'price': 10.4}, {'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#4', 'price': 13.67}, {'name': 'product#5', 'price': 16.45}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}, {'name': 'product#9', 'price': 38.68}, {'name': 'product#10', 'price': 45.56}]
print(f'customers: {customers}')    # [{'name': 'Jose', 'age': 59}, {'name': 'Maria', 'age': 32}, {'name': 'Joao', 'age': 77}, {'name': 'Pedro', 'age': 41}, {'name': 'Paulo', 'age': 56}, {'name': 'Tiago', 'age': 31}, {'name': 'Isaias', 'age': 48}, {'name': 'Mateus', 'age': 65}, {'name': 'Andre', 'age': 61}, {'name': 'Tadeu', 'age': 52}]
print(f'list_nums: {list_nums}')    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('\n2. Filter Data - Use filter(lambda expression) - New list with numbers greather than 5\n')

filter_new_list_nums = filter(lambda x: x>5, list_nums)
print(f'filter_new_list_nums: {filter_new_list_nums}')                # <filter object at 0x0000025FAE93D9E8>
print(f'list(filter_new_list_nums): {list(filter_new_list_nums)}')    # [6, 7, 8, 9, 10]


print('\n3. Filter Data - Use list comprehension - New list with numbers greather than 5\n')

new_list_nums = [x for x in list_nums if x > 5]
print(f'new_list_nums: {new_list_nums}')    # [6, 7, 8, 9, 10]


print('\n4. Filter Data - Use filter(lambda expression) - New list with products price greather than 50.00\n')

filter_new_customers = filter(lambda p: p['price'] > 50.0, products)
print(f'filter_new_products: {filter_new_customers}')              # <filter object at 0x000002191EB69710>
print(f'list(filter_new_products): {list(filter_new_customers)}')  # [{'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}]


print('\n4. Filter Data - Use filter(lambda function) - New list with products price greather than 50.00\n')

def filter_price_gt_50(p):
    if p['price'] > 50.0:
        return True

filter_new_customers = filter(filter_price_gt_50, products)
print(f'filter_new_products: {filter_new_customers}')              # <filter object at 0x000002191EB69748>
print(f'list(filter_new_products): {list(filter_new_customers)}')  # [{'name': 'product#2', 'price': 80.4}, {'name': 'product#3', 'price': 50.8}, {'name': 'product#6', 'price': 98.2}, {'name': 'product#7', 'price': 91.85}, {'name': 'product#8', 'price': 72.3}]


print('\n5. Filter Data - Use filter(lambda function) - New list with customers categorizes age\n')

def filter_age_category(c):
    if c['age'] < 18 :
        c['age_category'] = 'juvenil'
    elif c['age'] >= 18 and c['age'] < 30 :
        c['age_category'] = 'jovem'
    elif c['age'] >= 30 and c['age'] < 50:
        c['age_category'] = 'adulto'
    else:
        c['age_category'] = 'idoso'
    return True

filter_new_customers = filter(filter_age_category, customers)
print(f'filter_new_customers: {filter_new_customers}')              # <filter object at 0x000001E8EF5C9780>
print(f'list(filter_new_customers): {list(filter_new_customers)}')  # [{'name': 'Jose', 'age': 59, 'age_category': 'idoso'}, {'name': 'Maria', 'age': 32, 'age_category': 'adulto'}, {'name': 'Joao', 'age': 77, 'age_category': 'idoso'}, {'name': 'Pedro', 'age': 41, 'age_category': 'adulto'}, {'name': 'Paulo', 'age': 56, 'age_category': 'idoso'}, {'name': 'Tiago', 'age': 31, 'age_category': 'adulto'}, {'name': 'Isaias', 'age': 48, 'age_category': 'adulto'}, {'name': 'Mateus', 'age': 65, 'age_category': 'idoso'}, {'name': 'Andre', 'age': 61, 'age_category': 'idoso'}, {'name': 'Tadeu', 'age': 52, 'age_category': 'idoso'}]
