#
# filename   : lab-04-primitive-datatype-int-float-bool.py
# Description: Primitive int float and boolean datatype
# Docs       :  * https://docs.python.org/3/contents.html
#               * https://docs.python.org/3.9/reference/index.html
#

# str   - string  - textos 'assim' ou "assim"
# int   - inteiro - 1234567 ou 0 ou -1 ou 1000 ou -1000
# float - real/float point - 10.50 ou 3.141572
# bool  - boolean - True/False 10 == 10

print("Josemar", type("Josemar"))   # Josemar <class 'str'>
print("10", type("10"))             # 10 <class 'str'>
print(10, type(10))                 # 10 <class 'int'>
print(-1, type(-1))                 # -1 <class 'int'>
print(3.141572, type(3.141572))     # 3.141572 <class 'float'>
print(1==1, type(1==1))             # True <class 'bool'>
print(bool(0), type(bool(0)))       # False <class 'bool'>
print(bool('qualquer coisa'), type(bool('qualquer coisa')))  # True <class 'bool'>
print(float('10.0'))                # 10.0

# nome: str
print('Josemar', type('Josemar'))   # Josemar <class 'str'>

# idade: int
print(52, type(52))                 # 52 <class 'int'>

# altura: float
print(1.69, type(1.69))             # 1.69 <class 'float'>

# maior de idade
print(52>=18, type(52>=18))         # True <class 'bool'>