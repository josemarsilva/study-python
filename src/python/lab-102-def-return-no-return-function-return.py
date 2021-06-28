#
# filename   : lab-102-def-return-no-return-function-return.py
# Description: functions
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#

print('\n# 1. Return value and No Returns\n')

def division(n1, n2):
    if n2 > 0:
        return n1 / n2


# call
result = division(10, 2)
print('result = division(10, 2): ', result )  # result = division(10, 2):  5.0

result = division(10, 0)    # result is None
if result:
    print('result = division(10, 0): ', result) # NOT PRINTED
else:
    print('result = division(10, 0): Unable to calculate division() !')


print('\n#2. Return an entire function\n')

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def subtract(x,y):
    return x - y

def division(x,y):
    return x / y

def operation(operator = '+', x = 0, y = 0):
    if operator == '*':
        return multiply(x, y)
    elif operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '/':
        return division(x, y)
    else:  # default
        return add(x, y)


# calling function

print( type(operation()) )          # <class 'int'>
print( type(operation('+', 1, 2)) ) # <class 'int'>
print( type(operation('*', 1, 2)) ) # <class 'int'>
print( type(operation('-', 1, 2)) ) # <class 'int'>
print( type(operation('/', 1, 2)) ) # <class 'float'>
