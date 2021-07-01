#
# filename   : lab-121-exception-handling-try-except-raise-exception.py
# Description:
# Docs       :  * https://docs.python.org/3/whatsnew/2.6.html#pep-3110-exception-handling-changes
#               * https://docs.python.org/3/library/exceptions.html
#
from setuptools.command.easy_install import current_umask

print('\n#1. Exception handling - try except\n')

try:
    num = int(input('Digite um numero: '))  # Error occurs if value as not numeric
    a = []
    print('a = []; a[10] ... xii t happens')
    print(a[10])    # Error occurs list index out of range
    print(variavel_nao_declarada)           # NameError: name 'variavel_nao_declarada' is not defined
    # BEGIN - try except block inside
    try:
        print('try except inside try except')
        division_by_zero_error = 1 / 0
    except: # Exception id can be ommited - this means any exception but you will not know what
        print('Except inside NameError block')
    # END - try except block inside
except NameError:   # only this exception was triggered
    print('Exception de variável não declarada foi capturada e tratada!')
    print('O programa nao vai parar de executar ... uhuuuuu !!!')
except (IndexError, KeyError):
    print('Ocorreu uma destas duas exceptions: (IndexError, KeyError)')
except Exception as e:  # any other exception was triggered
    print('Ocorreu uma outra excecao qualquer: ', e)
else:
    print('Seu codigo foi executado com sucesso sem nenhuma exception')
finally:
    print('Em todos os casos o finally: sera executado')

print('segue o barco ...')


print('\n#2. Exception handling - Dica todas as classes de erro\n')

print('todas as classes de error terminam com "Error" ')


print('\n#3. Raise exception - custom exceptions \n')

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print('ZeroDivisionError exceptions was raised ')
        raise  # this will raise the same exception ZeroDivsionError


def custom_exception_zero_is_value_error(a):
    if a == 0:
        raise ValueError

# call

try:
    custom_exception_zero_is_value_error(1)  # ok
    custom_exception_zero_is_value_error(0)  # ValueError
except:
    print('Exception Value Error during execution of custom_exception_zero_is_value_error()')


print('\n#4. Nested try-except block \n')

def convert_to_int_or_float(v):
    try:
        return int(v)
    except:
        try:
            return float(v)
        except:
            return None

# call

num = convert_to_int_or_float(input('Digite um numero: '))

if num:
    print(f'Parabens! {num}  é numerico (int or float)')
else:
    print(f'Você errou porque deveria ser numerico (int or float)')
