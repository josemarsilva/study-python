#
# filename   : aula-107-tuple-vs-list.py
# Description: tuples
# Docs       : - https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
#              - https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple
#

print('\n# 1.Difference between Tuple and List\n')

print('* List: values can be changed')
print('* Tuple: values can NOT be changed. You can NOT add, modify, delete ')

print('\n# 2.Tuple\n')

t1 = (0, True, 'two', 3, 4, 5)
t2 = 1, 2, 3, 4, 5
t3 = 1,

print('t1: ', t1) # (0, True, 'two', 3, 4, 5)
print('t2: ', t2) # (1, 2, 3, 4, 5)
print('type(t1), type(t2), type(t3): ', type(t1), type(t2), type(t3)) # <class 'tuple'> <class 'tuple'> <class 'tuple'>

print('\n# 3. Tuple accessing elementes by index\n')

# index: 0  1  2  3  4
# value: 1  2  3  4  5
print('t2[0]    : ', t2[0])      # 1
print('t2[1:]   : ', t2[1:])     # (2, 3, 4, 5)
print('t2[2:3]  : ', t2[2:3])    # (3,) # returns a tuple of only one element
print('t2[2:4]  : ', t2[2:5])    # (3, 4, 5)
print('t2[2:99] : ', t2[2:99])   # (3, 4, 5)


print('\n# 4. Tuple operations\n')

t1 = 1, 3, 5, 7, 9
t2 = 2, 4, 6, 8, 10
t3 = t1 + t2
print('t1         : ', t1)  # (1, 3, 5, 7, 9)
print('t2         : ', t2)  # (2, 4, 6, 8, 10)
print('t3         : ', t3)  # (1, 3, 5, 7, 9, 2, 4, 6, 8, 10)
print('sorted(t3) : ', sorted(t3))


print('\n# 5. Tuple unpacking elements\n')

element1, element2, *elements, element10 = sorted(t3)
print('element1  : ', element1)     # 1
print('element2  : ', element2)     # 2
print('*elements : ', elements)     # [5, 7, 9, 2, 4, 6, 8, 10]
print('element10  : ', element10)   # 10

print('\n# 6. Tuple change values require convert to list\n')

print('t1         : ', t1)  # (1, 3, 5, 7, 9)
try:
    t1[0] = -1 # TypeError: 'tuple' object does not support item assignment
except:
    print('TypeError: \'tuple\' object does not support item assignment')

list_of_t1 = list(t1)
list_of_t1[0] = -1
t1 = tuple(list_of_t1)
print('type(t1)         : ', type(t1))          # <class 'tuple'>
print('t1               : ', t1)                # (-1, 3, 5, 7, 9)
print('type(list_of_t1) : ', type(list_of_t1))  # <class 'list'>
print('list_of_t1       : ', list_of_t1)        # [-1, 3, 5, 7, 9]
