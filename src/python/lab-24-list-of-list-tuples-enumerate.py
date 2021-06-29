#
# filename   : lab-24-list-of-list-tuples-enumerate.py
# Description: Lists
# Docs       : https://docs.python.org/3/whatsnew/2.0.html#list-comprehensions
#

print('\n# 1. list of list, tuples, enumerate \n')

lista_de_lista = [
    # index (0)
    #    0           1          2         3        4           5           6            7              8          9        10          11          12
    ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela'],
    # index (1)
    #    0            1               2            3
    ['Canadá', 'Estados Unidos', 'Groenlândia', 'México'],
    # index (2)
    #    0            1              2                3               4             5
    [ 'Angola', 'Cabo Verde', 'Guiné-Bissau', 'Guiné Equatorial', 'Moçambique', 'São Tomé e Príncipe' ]
]

# 1. List of Lists - each index has another list

print('lista_de_lista: ', lista_de_lista)
print('lista_de_lista[0]: ', lista_de_lista[0])
print('lista_de_lista[1]: ', lista_de_lista[1])
print('lista_de_lista[2]: ', lista_de_lista[2])


print('\n# 2. Enumeration of a list\n')

enum_lista_de_lista = enumerate(lista_de_lista)
print('enum_lista_de_lista: ', enum_lista_de_lista)
            # enum_lista_de_lista:  <enumerate object at 0x000001416604ACF0>
            # Não foi bem o que queriamos, afinal mostrar a posicao
            # de memoria com o conteudo da lista não ajuda muito

print('list(enum_lista_de_lista): ', list(enum_lista_de_lista))
    # [
    #   (0, ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']),
    #   (1, ['Canadá', 'Estados Unidos', 'Groenlândia', 'México']),
    #   (2, ['Angola', 'Cabo Verde', 'Guiné-Bissau', 'Guiné Equatorial', 'Moçambique', 'São Tomé e Príncipe'])
   # ]

for key, value in enumerate(lista_de_lista):
    print('(key,value): ', key, ', ',  value)   # (key,value):  0 ,  ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']
                                                # (key,value):  1 ,  ['Canadá', 'Estados Unidos', 'Groenlândia', 'México']
                                                # (key,value):  2 ,  ['Angola', 'Cabo Verde', 'Guiné-Bissau', 'Guiné Equatorial', 'Moçambique', 'São Tomé e Príncipe']



print('\n# 3. Tuple index()\n')

t1 = ('amarelo', 'azul', 'vermelho')
print('t1: ', t1)
print('t1.index(\'amarelo\'): ', t1.index('amarelo'))   # 0
print('t1.index(\'azul\'): ', t1.index('azul'))         # 1
print('t1.index(\'vermelho\'): ', t1.index('vermelho')) # 2
print('t1[0]: ', t1[0])                                 # amarelo
print('t1[1]: ', t1[1])                                 # azul
print('t1[2]: ', t1[2])                                 # vermelho
