#
# filename   : aula-27-conditional-expression-ternary-operation.py
# Description: Conditional expression, ternary operation
# Docs       : https://docs.python.org/3/reference/expressions.html?highlight=ternary#conditional-expressions
#

# 1. Conditional expression - ternary operation

is_logged = True

if is_logged:
    msg = 'User IS logged'
else:
    msg = 'User IS NOT logged'

print(msg)  # User IS logged

msg = 'User IS logged' if is_logged else 'User NOT IS logged'
print(msg)  # User IS logged


# 2. Operations using or

alguma_coisa = input('Digite alguma coisa(a): ')
if alguma_coisa:  # testa se vazio
    print(f'Você digitou {alguma_coisa}')   # Você digitou a
else:
    print(f'Você ERROU !!! Eu disse para digitar algo')


# 3. More than one operation using or
outra_coisa = input('Digite outra coisa(vazio): ')
print(outra_coisa or 'Você esqueceu de digitar')  # Você esqueceu de digitar

a = 0
b = None
c = False
d = []
e = {}
f = ''
g = 'qualquer coisa diferente de vazio'
h = 1
i = True

expressao = a or b or c or d or e or f or g  # primeira expressao nao vazia é 'g'
print(f'expressao: {expressao}')  # qualquer coisa diferente de vazio