#
# filename   : lab-23-split-join-enumerate-tuples-unpackage.py
# Description: Funcoes split(), join(), enumerate()
# Docs       :  * https://docs.python.org/3/howto/regex.html#splitting-strings
#               * https://docs.python.org/3.9/reference/index.html
#

# 1. Split e Join
from operator import index

texto = 'Capitu traia mesmo ou eram os olhos de Bentinho?'
lista_palavras = texto.split(' ')
lista_numeros = [ 'um',  'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
lista_numeros_joinned = ','.join(lista_numeros)

print(f'texto                : {texto}')             # Capitu traia mesmo ou eram os olhos de Bentinho?
print(f'lista_palavras       : {lista_palavras}')    # ['Capitu', 'traia', 'mesmo', 'ou', 'eram', 'os', 'olhos', 'de', 'Bentinho?']
print(f'lista_numeros        : {lista_numeros}')     # ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
print(f'lista_numeros_joinned: {lista_numeros_joinned}')

# 2. Enumerate

for indice, valor in enumerate(lista_numeros):
    print(f'indice: {indice}, valor: {valor}')  # indice: 0, valor: um, indice: 1, valor: dois, ...


# 3. Unpackage

lista_simples = [ 'um', 'dois', 'tres', 'quatro', 'cinco']
e1, e2, e3, e4, e5 = lista_simples

print('lista_simples: ', lista_simples) # lista_simples:  ['um', 'dois', 'tres', 'quatro', 'cinco']
print('  e1: ', e1)                     # e1: um
print('  e2: ', e2)                     # e2: dois
print('  e3: ', e3)                     # e3: tres
print('  e4: ', e4)                     # e4: quatro
print('  e5: ', e5)                     # e5: cinco
