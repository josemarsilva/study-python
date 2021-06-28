#
# filename   : lab-101-def-function-create-use-arguments-default-return.py
# Description: functions
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#

print('\n# 1. Using functions\n')

print('Hello')  # print() is a function

print('\n# 2. Creating function\n')


def function_name(argument_name):   # function has a name and a list of arguments
    print(argument_name)            # this function prints a argument

print('- calling function_name(argument_name) using blablabla')
function_name('blablabla')  # blablabla


print('\n3. Creating function with defaults arguments\n')

def say_hello(msg='Hello', name='You'):
    print(msg, name)

# call
say_hello('Hi', 'Mr. Josemar')          # Hi Mr. Josemar
say_hello()                             # Hello You
say_hello('Hi')                         # Hi You
say_hello(name='Meu Nome', msg='Olá')   # Olá Meu Nome


print('\n#4. Creating function with return\n')

def open_text(msg ='Hello', name='You', body='You are special for Python', close='bye'):
    text = msg + name + ', \n' + body + '\n' + close
    return text


print('\n#5. None is returned for function with no return\n')

x = say_hello()
print(f'x = {x}')