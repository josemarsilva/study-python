#
# filename   : lab-109-set-add-update-clear-discard-union-intersection-difference.py
# Description: Dictionary
# Docs       : - https://docs.python.org/3/tutorial/datastructures.html#sets
#

print('\n# 1. Set\n')

print(  '  * Set are UNMUTABLES')
s1 = {1,2,3,4,5}
print('s1: ', s1)   # {1, 2, 3, 4, 5}
s1.add(6)
s1.add(7)
print('s1: ', s1)   # {1, 2, 3, 4, 5, 6, 7}
s1.discard(2)
s1.discard(4)
s1.discard(6)
print('s1: ', s1)   # {1, 3, 5, 7}
s1.update('iteravel')
print('s1: ', s1)   # {1, 3, 'a', 5, 'l', 7, 't', 'i', 'v', 'e', 'r'}
    # set does not respect order


print('\n# 2. Set - using set to remove duplicates from list\n')

list1 = [5,3,2,5,4,1,2,3,1,4,2,5,2,5,1,3,5,2,1,4,5,4]
set1 = set(list1)
print('list1: ', list1)
print('set1 : ', set1)
list1_unique = list(set1)
print('list1_unique : ', list1_unique)


print('\n# 3. Set - operations: union |, intersection &, difference\n')

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7}

# Set Union remove duplicity and result a unique values set
set3 = set1 | set2;
print('set3 : ', set3)  # {1, 2, 3, 4, 5, 6, 7}

# Set Intersection results every element present in both set's
set4 = set1 & set2;
print('set4 : ', set4)  # {1, 2, 3, 4, 5}

# Set Difference results elements ramining from subraction
set5 = set3 - set1
print('set5 : ', set5)  # {6, 7}
set6 = {1,3,5,7,9} # 9 does not exists in set3
set7 = set3 - set6
print('set7 : ', set7)  # {2, 4, 6}

# Set Simmetric Difference (Union - Intersection) results elements that exists in both set's individually
set8 = {1,2,3,4,5}  # {1,2} not in set9
set9 = {3,4,5,6,7}  # {6,7} not in set8
set10 = set8 ^ set9
print('set10 : ', set10)  # {1, 2, 6, 7}

