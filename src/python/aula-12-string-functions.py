#
# filename   : aula-12-string-functions.py
# Description: String functions
#

str_1 = "Ola"
str_2 = "1234567890"
str_3 = "123.567.91011"

print("str_1          : ", str_1)
print("str_2          : ", str_2)
print("str_3          : ", str_3)
print("len(str_1)     : ", len(str_1))

# __ + nome-da-funcao + __ injeta o nome da funcao na variavel
print("str_1.__len__(): ", str_1.__len__())

# Input de valores nao garante o datatype numerico
num_1 = input("Entre com o valor de num_1: " )
num_2 = input("Entre com o valor de num_2: " )

# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_3 = num_1 + num_2
    print(f'{num_1} + {num_2} = {num_3} ')
else:
    print(f'valores não são numéricos: {num_1}  {num_2} ')
