#
# filename   : aula-08-user-input-casting-datatype.py
# Description: User input casting datatype
# Docs       : https://docs.python.org/3/contents.html
#

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nasc = 2021 - int(idade)

print(f"O usuário digitou {nome} tem {idade} anos e nasceu em {ano_nasc}" )