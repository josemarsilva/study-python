#
# filename   : lab-16-formatting-values.py
# Description: format(), f''. Examples: :s string, :d inteiro, :f decimais, :(number-of-chars)
# Docs       :  * https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals
#               * https://docs.python.org/3.9/reference/index.html
#

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print("num_1 / num_2 = ", divisao)  # num_1 / num_2 =  3.3333333333333335
print('{}'.format(divisao))         # 3.3333333333333335
print('{:.2f}'.format(divisao))     # 3.33
print( f'{divisao:.2f}' )           # 3.33

num_4 = 4
print(f'{num_4}')           # 4
print(f'{num_4:5}')         #     4
print(f'{num_4:0>5}')       #00004
print(f'{num_4: >10}')      #         4
print(f'{num_4:0<10}')      #4000000000
print(f'{num_4:0>10.2f}')   #0000004.00

nome = 'Josemar Silva'
print(f'{nome}')                            # Josemar Silva
nome_formatado_1 = '{:.>20}'.format(nome)
print(nome_formatado_1)                     # .......Josemar Silva
nome_formatado_2 = '{:@<20}'.format(nome)
print(nome_formatado_2)                     # Josemar Silva@@@@@@@
