#
# filename   : lab-12-string-functions.py
# Description: String functions - len(), isdigit(), upper(), lower(), title()
# Docs       : https://docs.python.org/3/contents.html
#
import string

print('\n# 1. String - len(), isdigit() \n')

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

print('\n# 2. String - upper(), lower(), title(), capitalize(), find(), replace() \n')

str_1 = 'aeiou asdfg hjklç qwert yuiop ZXCVB nM,.;'
str_2 = 'aeiou'
str_3 = '  palavras com espacos amais a esquerda e a direita '
print('str_1              : ', str_1)               # aeiou asdfg hjklç qwert yuiop ZXCVB nM,.;
print('str_2              : ', str_2)               # aeiou
print('str_3              : ', str_3)               #   palavras com espacos amais a esquerda e a direita
print('str_1.upper()      : ', str_1.upper())       # AEIOU ASDFG HJKLÇ QWERT YUIOP ZXCVB NM,.;
print('str_1.title()      : ', str_1.title())       # Aeiou Asdfg Hjklç Qwert Yuiop Zxcvb Nm,.;
print('str_1.capitalize() : ', str_1.capitalize())  # Aeiou asdfg hjklç qwert yuiop zxcvb nm,.;
print('\'>\' + str_3.strip() + \'<\'      : ', '>' + str_3.strip() + '<')
                                                    # >palavras com espacos amais a esquerda e a direita<

print('str_1.find(\'s\')  : ', str_1.find('s'))     # 7
print('str_1.find(\'s\')  : ', str_2.find('s'))     # -1
print('str_1.replace(\'a\',\'*\') : ', str_1.replace('a','*'))
                                                    # *eiou *sdfg hjklç qwert yuiop ZXCVB nM,.;


print('\n# 3. String - Template \n')

print('string.ascii_letters:   ' ,string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print('string.ascii_lowercase: ' ,string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print('string.ascii_uppercase: ' ,string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print('string.digits:          ' ,string.digits)            # 0123456789
print('string.hexdigits:       ' ,string.hexdigits)         # 0123456789abcdefABCDEF
print('string.octdigits:       ' ,string.octdigits)         # 01234567
print('string.printable:       ' ,string.printable)         # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print('string.punctuation:     ' ,string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print('string.whitespace:      ' ,string.whitespace)        #
