#
# filename   : aula-106-lambda-expression-anonymous-function.py
# Description: variable scopes: global vs function local
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
#

print('\n# 1.Anonymous functions\n')

list_of_product_price = [
    ['Product #1', 30.4],
    ['Product #2', 23.1],
    ['Product #3', 31.5],
    ['Product #4', 24.2],
    ['Product #5', 25.3]
]

print('list_of_product_price       : ', list_of_product_price)
    # [['Product #1', 30.4], ['Product #2', 23.1], ['Product #3', 31.5], ['Product #4', 24.2], ['Product #5', 25.3]]

list_of_product_price.sort()
print('list_of_product_price(after sort): ', list_of_product_price)
        # [['Product #1', 30.4], ['Product #2', 23.1], ['Product #3', 31.5], ['Product #4', 24.2], ['Product #5', 25.3]]
        # It was not we expected! Nothing happens, because sort elements are another list

def func_price_of_item(item):
    return item[1]  # 0=Product Name; 1=Price

list_of_product_price.sort(key=func_price_of_item)
print('list_of_product_price(after sort func_price_of_item): ', list_of_product_price)
        # [['Product #2', 23.1], ['Product #4', 24.2], ['Product #5', 25.3], ['Product #1', 30.4], ['Product #3', 31.5]]
        # It's OK now! sorted ASC by price


list_of_product_price.sort(key=func_price_of_item, reverse=True)
print('list_of_product_price(after sort func_price_of_item): ', list_of_product_price)
        # [['Product #3', 31.5], ['Product #1', 30.4], ['Product #5', 25.3], ['Product #4', 24.2], ['Product #2', 23.1]]
        # It's OK now! sorted ASC by price


print('\n# 2.Lambda expression\n')

list_of_product_price = [
    ['Product #1', 30.4],
    ['Product #2', 23.1],
    ['Product #3', 31.5],
    ['Product #4', 24.2],
    ['Product #5', 25.3]
]


list_of_product_price.sort(key=lambda item: item[1])
print('list_of_product_price(after sort lambda): ', list_of_product_price)
        # [['Product #2', 23.1], ['Product #4', 24.2], ['Product #5', 25.3], ['Product #1', 30.4], ['Product #3', 31.5]]
        # It's OK now! sorted ASC LAMBDA and it was not necessary to build another function
