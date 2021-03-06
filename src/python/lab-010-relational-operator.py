#
# filename   : lab-10-relational-operator.py
# Description: Relational operator: == <> >= <= !=
# Docs       :  * https://docs.python.org/3/contents.html
#               * https://docs.python.org/3.9/reference/index.html
#

# Operadores relacionais:
# == <> >= <= !=

num_1 = 1 # int
num_2 = 2 # int
num_3 = 3 # int
num_4 = 4 # int

str_1 = "abcde"
str_2 = "fghij"

expressao = (num_1 == num_2)
print(expressao)

expressao = (num_1 < num_2)
print(expressao)

expressao = (num_3 >= num_2)
print(expressao)

expressao = (num_3 != num_2)
print(expressao)

expressao = (str_1 == str_2)
print(expressao)
