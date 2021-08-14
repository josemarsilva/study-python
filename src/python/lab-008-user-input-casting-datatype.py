#
# filename   : lab-08-user-input-casting-datatype.py
# Description: User input casting datatype
# Docs       :  * https://docs.python.org/3/contents.html
#               * https://docs.python.org/3.9/reference/index.html
#

import getpass

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nasc = 2021 - int(idade)

password = getpass.getpass("Qual a senha do seu banco? ")

print(f"O usuário digitou {nome} tem {idade} anos e nasceu em {ano_nasc} e a senha do banco é {password}" )
