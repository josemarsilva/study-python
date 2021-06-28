#
# filename   : lab-112-iterable-iterator-generator-yield.py
# Description: Dictionary
# Docs       : https://docs.python.org/3/tutorial/datastructures.html
#

print('\n# 1. Iterable, iterator and generate iterable objects\n')

list_iterable_obj = [1,2,3,4,5]
number_non_iterable_obj = 12345
string_iterable_obj = '12345'

print('hasattr(list_iterable_obj,\'__iter__\'): ', hasattr(list_iterable_obj,'__iter__'))              # True
print('hasattr(number_non_iterable_obj,\'__iter__\'): ', hasattr(number_non_iterable_obj,'__iter__'))  # False
print('hasattr(string_iterable_obj,\'__iter__\'): ', hasattr(string_iterable_obj,'__iter__'))          # True
print('')
print('hasattr(list_iterable_obj,\'__next__\'): ', hasattr(list_iterable_obj,'__next__'))              # True
print('hasattr(number_non_iterable_obj,\'__next__\'): ', hasattr(number_non_iterable_obj,'__next__'))  # False
print('hasattr(string_iterable_obj,\'__next__\'): ', hasattr(string_iterable_obj,'__next__'))          # True

print('\n# 2. Transfor object iterable list into iterator object \n')
iter_list_iterable_obj = iter(list_iterable_obj)
print('list_iterable_obj           : ', list_iterable_obj)             # [1, 2, 3, 4, 5]
print('next(iter_list_iterable_obj): ', next(iter_list_iterable_obj))  # 1
print('next(iter_list_iterable_obj): ', next(iter_list_iterable_obj))  # 2
print('next(iter_list_iterable_obj): ', next(iter_list_iterable_obj))  # 3


print('\n# 3. List allocates memory for objects\n')
import sys
l1 = list(range(10))    # range(10): [0,1,2, ... 9]
l2 = list(range(100))   # range(100): [0,1,2, ... 99]
l3 = list(range(1000))  # range(1000): [0,1,2, ... 999]
print('l1               : ', l1)                # [0, 1, 2, .. , 9]
print('sys.getsizeof(l1): ', sys.getsizeof(l1)) # 200
print('l2               : ', l2)                # [0, 1, 2, .. , 99]
print('sys.getsizeof(l2): ', sys.getsizeof(l2)) # 1008
print('l3               : ', l3)                # [0, 1, 2, .. , 999]
print('sys.getsizeof(l3): ', sys.getsizeof(l3)) # 9112


print('\n# 4. List allocates memory for objects - iterators generator can reduce memory allocation\n')
import sys
import time

def generate():
    for n in range(100):
        yield n         # lazy evaluation
        time.sleep(0.1) # sleep or 1/10 seconds

# call
g = generate()
print('hasattr(g, \'__next__\') : ', hasattr(g, '__next__'))
print('hasattr(g, \'__iter__\') : ', hasattr(g, '__iter__'))

for element in g:
    print(element)

print('\n# 5. List vs Generator\n')
import sys

l1 = [x for x in range(1000)]
print('type(l1):', type(l1))                    # <class 'list'>
print('sys.getsizeof(l1):', sys.getsizeof(l1))  # 9024
print('')
l2 = (x for x in range(1000))
print('type(l2):', type(l2))                    # <class 'generator'>
print('sys.getsizeof(l2):', sys.getsizeof(l2))  # 88


