#
# filename   : lab-05-arithmetics-operator.py
# Description: Arithmetics operators +, -, *, /, //, %
# Docs       :  * https://docs.python.org/3/contents.html
#               * https://docs.python.org/3.9/reference/index.html
#

print('\n# 1. Arithmetics operation \n')

print(10 * 10)   # multiplicação
print(10 + 10)   # adição
print(10 - 10)   # subtração
print(10 / 2)    # divisao
print(10.5 / 3)  # divisao ponto flutuante
print(10 / 3)    # divisao ponto flutuante
print(10 // 3)   # divisao inteira
print(10 % 3)    # resto da divisao
print(10**2)     # exponenciacao
import math
print(math.sqrt(81))  # radiciacao ( raiz quadrada )

print(10 * "Josemar")  # operador de repeticao
print('5' + '5')       # concatenate

print('Josemar tem ' + str(52) + ' anos')

# alteração de precedência de operadores
print(5+2*10)    # precedencia de multiplicacao e divisao resolvida antes
print((5+2)*10)  #


print('\n# 2. round(), trunc() \n')
print('134/34432 :', 134/34432)   # 0.003891728624535316
print(':', round(134/34432,5))    # 0.00389
print(':', round(134/34432,4))    # 0.0039
import math
print(':', math.trunc(134/34432*10**5)/10**5)  # 0.00389
print(':', math.trunc(134/34432*10**4)/10**4)  # 0.0038
