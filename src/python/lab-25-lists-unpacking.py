#
# filename   : lab-25-lists-unpacking.py
# Description: Lists
# Docs       :  * https://docs.python.org/3/whatsnew/2.0.html#list-comprehensions
#               * https://docs.python.org/3.9/reference/index.html
#


# 1. Unpacking list
list = [ 'amarelo', 'azul', 'vermelho']

element1, element2, element3 = list

print('list :', list)
print('list[0] :', list[0])
print('list[1] :', list[1])
print('list[2] :', list[2])
print('element1 : ', element1)
print('element2 : ', element2)
print('element3 : ', element3)

# 2. Unpacking list - restrictions

try:
    print('Unpack must mach number of elements! - ValueError: too many values to unpack (expected 2)')
    element1, element2  = list  # ValueError: too many values to unpack (expected 2)
                                # Unpack must mach number of elements!
except:
    pass

try:
    print('Unpack must mach number of elements! - ValueError: not enough values to unpack (expected 4, got 3)')
    element1, element2, element3, element4  = list  # ValueError: not enough values to unpack (expected 4, got 3)
                                                    # Unpack must mach number of elements!
except:
    pass


# 3. Unpacking list advanced - some elements of start

element1, *list_of_others_elements  = list # Unpack first element and all other elements in another list

print('element1               : ', element1)                # amarelo
print('list_of_others_elements: ', list_of_others_elements) # ['azul', 'vermelho']

# 4. Unpacking list advanced - some elements of end

element1, *list_of_others_elements, element_last = list  # Unpack first element and all other elements in another list

print('element1               : ', element1)                # amarelo
print('element_last           : ', element_last)            # vermelho
print('list_of_others_elements: ', list_of_others_elements) #['azul']
