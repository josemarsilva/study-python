#
# filename   : lab-04-primitive-datatype-int-float-bool.py
# Description: Primitive int float and boolean datatype
# Docs       : https://docs.python.org/3/contents.html
#

# str   - string  - textos 'assim' ou "assim"
# int   - inteiro - 1234567 ou 0 ou -1 ou 1000 ou -1000
# float - real/float point - 10.50 ou 3.141572
# bool  - boolean - True/False 10 == 10

print("Josemar", type("Josemar"))
print("10", type("10"))
print(10, type(10))
print(-1, type(-1))
print(3.141572, type(3.141572))
print(1==1, type(1==1))
print(bool(0), type(bool(0)))
print(bool('qualquer coisa'), type(bool('qualquer coisa')))
print(float('10.0'))

# nome: str
print('Josemar', type('Josemar'))

# idade: int
print(52, type(52))

# altura: float
print(1.69, type(1.69))

# maior de idade
print(52>=18, type(52>=18))