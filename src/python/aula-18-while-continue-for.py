#
# filename   : aula-18-while-continue.py
# Description: String [index], slice [start:end]
# Docs       : https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
#

# 1. While, break, continue

x = 1
y = 1
while x <= 100:
    if x == 5:
        break   # sai do loop quando chegar no 5
    nome = input("Qual o seu nome? ")
    print(f'Olá {nome} !')
    x = x + 1   # x+ = 1
    continue    # pula o resto do loop
    y = y + 1


# 2. While .. Else

x = 1
while x < 5:
    y = 1
    while y < 10:
        print(f'[{x},{y}]: ')
        if y == 2:
            break
        y += 1
    else:
        print(f'Else(y)')
    print(f'Acabou(y)')
    x += 1
else:
    print(f'Else(x)')
print('Acabou(x)')

