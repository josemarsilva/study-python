#
# filename   : aula-14-try-except.py
# Description: Try ... Except ...
# Docs       : https://docs.python.org/3/whatsnew/2.5.html#pep-341-unified-try-except-finally
#

num1 = input("Digite numero #1 (digite 1.05): ")
num2 = input("Digite numero #2 (digite 3.1415): ")

try:
    float1 = float(num1)
    float2 = float(num2)
    print("num1 + num2 = ", (float1 + float2))
except:
    print("nao foi possivel converter num1 e num2 ( '" + num1 + "', '" + num2 + "' ) para efetuar a soma")
