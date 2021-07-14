#
# filename    : lab-202-decorators.py
# Description : Decorators
# Docs        :  * https://docs.python.org/3.9/reference/index.html
#

print('\n#1. Decorators - functions\n')

def function_say_hello():
    print('Hello!')
    # return implicity None

var_1 = function_say_hello

print(f'type(var_1)         : {type(var_1)}')              # <class 'function'>
print(f'var_1               : {var_1}')                    # <function function_say_hello at 0x0000022827FE3E18>
print(f'function_say_hello(): {function_say_hello()}')  # None
                                                        # Hello!


print('\n#2. Decorators - passing functions as parameter of a function\n')

# Decorated Function
def master(function_param):
    def slave():
        function_param()
        # return None is implicity
    return slave

# Decorator
def function_print_hello():
    print('Hello #1!')

var_2 = master(function_print_hello)

# invoke call function var_2()
var_2()                                 # Hello #1!

print(f'type(var_2): {type(var_2)}')    # <class 'function'>
print(f'var_2      : {var_2}')          # <function master.<locals>.slave at 0x000001AC297DFD08>
print(f'var_2()    : {var_2()}')        # None
                                        # Hello #1!

# here I redefine function
def function_print_hello(msg):
    print(msg)

# invoke call function_print_hello(msg):
function_print_hello('say hello!') # say hello!

function_print_hello = var_2()  # Hello #1!

print('\n#3. Decorators - usar decorador para calcular tempo de uma funcao\n')

from time import time
from time import sleep

# Decorated function
def run_a_function(function_name):
    def function_to_run(*args, **kwargs):
        start_time = time()
        result =  function_name(*args, **kwargs)
        end_time = time()
        elapsed = (end_time - start_time)
        print(f'Function {function_name.__name__} elapsed {elapsed:.2f} sec')
        return result  # function_to_run()

    return function_to_run

# Decorator
@run_a_function
def sleep_seconds(seconds):
    for i in range(seconds):
        print(i + 1)
        sleep(1)

# invoke call function
sleep_seconds(10)

