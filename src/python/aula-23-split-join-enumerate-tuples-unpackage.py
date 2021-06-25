#
# filename   : aula-23-split-join-enumerate-tuples-unpackage.py
# Description: Funcoes split(), join(), enumerate()
# Docs       : https://docs.python.org/3/howto/regex.html#splitting-strings
#

texto = 'Capitu traia mesmo ou eram os olhos de Bentinho?'
lista_palavras = texto.split(' ')
lista_numeros_impares = [ 'um',  'tres', 'cinco', 'sete', 'nove']
lista_numeros_pares = [  'dois', 'quatro', 'seis', 'oito', 'dez']
lista_numeros = ','.join(lista_numeros_impares + lista_numeros_pares)

print(f'Dado o texto: {texto}')             # Capitu traia mesmo ou eram os olhos de Bentinho?
print(f'  - palavras: {lista_palavras}')    # ['Capitu', 'traia', 'mesmo', 'ou', 'eram', 'os', 'olhos', 'de', 'Bentinho?']
print(f'  - numeros : {lista_numeros}')     # um,tres,cinco,sete,nove,dois,quatro,seis,oito,dez

lista_simples = [ 'um', 'dois', 'tres', 'quatro', 'cinco']

