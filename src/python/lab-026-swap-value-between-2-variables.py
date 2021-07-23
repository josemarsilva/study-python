#
# filename   : lab-26-swap-value-between-2-variables.py
# Description: Lists
# Docs       :  * https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
#               * https://docs.python.org/3.9/reference/index.html
#

# 1. Swap values between 2 variables

x = 1
y = 'Python'
print(f'x={x}, y={y}')

x, y = y, x
print(f'x={x}, y={y}')

# 1. Swap values between more than 2 variables

x = 1
y = 'Python'
z = True
print(f'x={x}, y={y}, z={z}')
x, y, z = z, y, x
print(f'x={x}, y={y}, z={z}')
