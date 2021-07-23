#
# filename   : lab-02-print-separator-end.py
# Description: How to print separator
# Docs       :  * https://docs.python.org/3/contents.html
#               * https://docs.python.org/3.9/reference/index.html
#

print('Josemar', 'Silva', 'Outra coisa')        # Josemar Silva Outra coisa
print('Josemar', 'Silva', sep='-', end='###')
print('Josemar', 'Silva', sep='*', end='')      # Josemar-Silva###Josemar*Silva

# Python is case sensitive. Next command was commented to avoid run time error
# Print('Josemar')

print ('')
# Imprimir o CPF 824.172.070-18 usando separator e end
print('824', '172', '070', sep='.', end='-')
print('18')                                     # 824.172.070-18