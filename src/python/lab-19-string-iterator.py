#
# filename   : lab-19-string-iterator.py
# Description: String iterator
# Docs       : https://docs.python.org/3/library/stdtypes.html#iterator-types
#

#        0         1         2         3
#        0123456789012345678901234567890123456789
frase = 'O rato roeu a roupa do rei de Roma'
tamanho = len(frase)

print(f'Tamanho da frase: ', tamanho)       # 34 (inicio em 0)
print(f'Indice 3 da frase: ', frase[3])     # a


i = 0
while i < tamanho:
    print(f'[{i}]: ', frase[i])
    i += 1