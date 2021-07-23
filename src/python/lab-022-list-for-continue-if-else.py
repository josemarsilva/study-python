#
# filename   : lab-22-list-for-continue-if-else.py
# Description: Lists, for, continue, if else
# Docs       :  * https://docs.python.org/3/tutorial/introduction.html#lists
#               * https://docs.python.org/3.9/reference/index.html
#

list = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Bolivia', 'Chile', 'Peru', 'Venezuela', 'Colombia']
list_paises_com_b = []
cont_paises_com_b = 0
for element in list:
    if element.startswith('B'):
        cont_paises_com_b += 1
        list_paises_com_b.append(element)
        continue
    print(f'infelizmente o pais {element} não e o que estamos procurando!')

print(f'Na lista {list}')
print(f'  - ha {cont_paises_com_b} que iniciam com "B"' )
print(f'  - lista de paises: ', list_paises_com_b)