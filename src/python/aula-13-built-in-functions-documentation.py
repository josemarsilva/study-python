#
# filename   : aula-13-built-in-functions-documentation.py
# Description: Built in functions documentation - input(), isdecimal(), isdigit(), isnumeric(),
#              istitle(), isupper(), islower()
# Docs       : https://docs.python.org/3/library/stdtypes.html
#

# 1. Input default Data Type is string - Python do NOT convert to you

num1 = input("Digite numero #1 (digite 1): ")
num2 = input("Digite numero #2 (digite A): ")

print( "resultado: "  + num1 + num2 )  # Nao foi bem o que era esperado, foram concatenados os strings e nao somados numeros


# 2. Input default Data Type is string - Python do NOT check consistency for you

# num1 = int(num1) # OK converte 1 para numerico
# num2 = int(num2) # ValueError: invalid literal for int() with base 10: 'A':
# user input is NOT automatically consisted


# 2.1. Manually consist user input()

if num1.isdigit() and num2.isdigit() and not num1.isspace() and not num2.isspace():
    num1 = int(num1)
    num2 = int(num2)
    print("num1 + num2 = ", (num1 + num2) )
else:
    print("nao foi possivel converter num1 e num2 ( '" + num1 + "', '" + num2 + "' ) para efetuar a soma")

# 3. Built in functions - isdecimal(), isdigit(), isnumeric()

print("")

print( "'1234'.isdecimal()", '1234'.isdecimal() )
print( "'-1'.isdecimal()", '-1'.isdecimal() )
print( "'123.45'.isdecimal()", '123.45'.isdecimal() )
print( "'123,45'.isdecimal()", '123,45'.isdecimal() )
print( "''.isdecimal()", ''.isdecimal() )

print("")

print( "'1234'.isdigit()", '1234'.isdigit() )
print( "'-1'.isdigit()", '-1'.isdigit() )
print( "'123.45'.isdigit()", '123.45'.isdigit() )
print( "'123,45'.isdigit()", '123,45'.isdigit() )
print( "''.isdigit()", ''.isdigit() )

print("")

print( "'1234'.isnumeric()", '1234'.isnumeric() )
print( "'-1'.isnumeric()", '-1'.isnumeric() )
print( "'123.45'.isnumeric()", '123.45'.isnumeric() )
print( "'123,45'.isnumeric()", '123,45'.isnumeric() )
print( "''.isnumeric()", ''.isnumeric() )


# 4. Built in functions - istitle(), isupper(), islower()
print("")

print( "'Josemar Silva'.istitle()", '.Josemar Silva'.istitle() )
print( "'josemar'.istitle()", '.josemar'.istitle() )
print( "'JOSEMAR'.isupper()", 'JOSEMAR'.isupper() )
print( "'Josemar'.isupper()", 'Josemar'.isupper() )
print( "'josemar'.islower()", 'josemar'.islower() )

