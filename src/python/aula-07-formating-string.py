# aula7-formating-string.py

nome = "Josemar"      # str
idade = 52            # int
altura = 1.69         # float
e_maior = idade > 18  # boolean
peso = 73             # int
imc = peso / (altura* altura)

print(f'{nome} tem {idade} anos e seu imc é de {imc:.2f}')  # 2 casas decimais
print('{0} tem {1} anos e seu imc é de {2}' .format(nome, idade, imc))  # 2 casas decimais
