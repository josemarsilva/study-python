#
# filename   : lab-21-lists-index-slice-append-insert-pop-del-clear-extend.py
# Description: Lists
# Docs       : https://docs.python.org/3/tutorial/introduction.html#lists
#

# 1. Relembrando os tipos de dados

booleano_1 = True
booleano_2 = False
inteiro_1 = 1
inteiro_2 = 2
inteiro_3_ = -3
flutuante_1 = 3.141516
texto_1 = 'Josemar'
texto_2 = 'Josemar Furegatti de Abreu Silva'

# 2. Listas

# index    0  1  2  3  4
#         -5 -4 -3 -2 -1
lista_1 = [1, 2, 3, 4, 5]
lista_2 = ['azul', 'amarelo', 'vermelho' ]
lista_3 = [ -1, 0, True, 'dois', 'three', 'cuatro', 5 ]
lista_4 = [ -1, -0.0000000001, 'zero', 'one', 'dois', [ 1, 1, 1], 'cuatro', [1+1+1+1+1], lista_1 ]

print( 'lista_1: ', lista_1 )   # [1, 2, 3, 4, 5]
print( 'lista_2: ', lista_2 )   # ['azul', 'amarelo', 'vermelho']
print( 'lista_3: ', lista_3 )   # [-1, 0, True, 'dois', 'three', 'cuatro', 5]
                                # PS: Observe que sao tipos de dados diferentes, int, string, float
print( 'lista_4: ', lista_4 )   # [-1, -1e-10, 'zero', 'one', 'dois', [1, 1, 1], 'cuatro', [5], [1, 2, 3, 4, 5]]
                                # PS: Observe que os tipos sao diferentes, inclusive estrutura de listas dentro de listas

# 3. Index, Slice

print("")

print( 'lista_1[0]: ', lista_1[0] )                 # 1
print( 'lista_2[-1]: ', lista_2[-1] )               # 'vermelho'
                                                    # PS: Ultimo
print( 'lista_3.len: ', len(lista_3) )              # PS: tamanho da lista = quantidade de elementos
print( 'lista_3[::2]: ', lista_3[::2] )             # [-1, True, 'three', 5]
                                                    # PS: mostra, pula, mostra
print( 'lista_1[-2::-1]: ', lista_1[-2::-1] )       # lista_1[-2::-1]
                                                    # PS: invertida


# 4. List operations
print("")

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l3_alias = l3
l4 = [7, 8, 9, 10]


print('l1: ', l1)               # [1, 2, 3]
print('l2: ', l2)               # [4, 5, 6]
print('l3: ', l3)               # [1, 2, 3, 4, 5, 6]
                                # PS: Operator + concatenates lists
print('l3_alias: ', l3_alias)   # [1, 2, 3, 4, 5, 6]
print('l4: ', l4)               # [7, 8, 9, 10]

l4.append(11)
l4.append(12)
print('l4 (appended): ', l4)    # [7, 8, 9, 10, 11, 12]
                                # PS: append() adiciona um elemento ao final

l4.insert(0, -6)
print('l4 (appended): ', l4)    # [-6, 7, 8, 9, 10, 11, 12]
                                # PS: insert() coloca o novo elemento na posição passada como parametro
l4.insert(4, 9.999)
print('l4 (appended): ', l4)    # [-6, 7, 8, 9, 9.999, 10, 11, 12]
                                # PS: insert() coloca o novo elemento na posição passada como parametro

print('l3: ', l3)               # [1, 2, 3, 4, 5, 6]
print('l3_alias: ', l3_alias)   # [1, 2, 3, 4, 5, 6]

l3.append(7)
l3.append(8)
print('l3 (appended): ', l3)    # [1, 2, 3, 4, 5, 6, 7, 8]
                                # PS: appended() 7, 8 ao final
l3.pop()
print('l3 (appended, poped): ', l3)     # [1, 2, 3, 4, 5, 6, 7]
                                        # PS: pop() remove ultimo elemento

del(l3[2])
print('l3 (appended, deleted): ', l3)   # [1, 2, 3, 5, 6, 7]
                                        # PS: del(i) remove index position

print('l3_alias: ', l3_alias)           # [1, 2, 4, 5, 6, 7]
                                        # PS: que a atribuicao de listas é um ponteiro
                                        #     para para o endereco de memoria com a lista
                                        #     e nao uma copia da lista

l3.append(3)
l3.append(0)
l3.append(-1)
print('l3: ', l3)               # [1, 2, 4, 5, 6, 7, 3, 0, -1]
print('max(l3): ', max(l3))     #  7
print('min(l3): ', min(l3))     # -1

# 5. Iterable objects vs Lists

iterable_object = range(1, 5)
list_from_iterable_object = list(iterable_object)
print('iterable_object: ', iterable_object)                     # iterable_object
                                                                # PS: o retorno de range() é um objeto
                                                                #     iteravel e nao a lista propriamente
print('list_from_iterable_object: ', list_from_iterable_object) # [1, 2, 3, 4]

# 5.1. Somando os objetos atraves da iteracao entre seus elementos
print('Iterable objects - sum (elements)')
soma = 0
for element in list_from_iterable_object:
    print('(type,valor): ', type(element), ', ', element)    # ( <class 'int'>, 1 ) ...
    soma = soma + element

print('soma: ', soma)   # 45


# 5.2. Somando os objetos atraves da iteracao entre seus elementos
print('Iterable objects - print (elements)')
print('lista_3: ', lista_3)     # [-1, 0, True, 'dois', 'three', 'cuatro', 5]
for element in lista_3:
    print('(type,valor): ', type(element), ', ', element)

