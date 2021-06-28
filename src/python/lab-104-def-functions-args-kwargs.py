#
# filename   : lab-104-def-functions-args-kwargs.py
# Description: functions returns
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#

print('\n# 1. Functions def args - required\n')

def func_1(p1, p2, p3, p4, p5): # all arguments required and return None
    return

def func_2(p1, p2, p3, p4, p5): # all arguments required and return tuple of all arguments
    return (p1, p2, p3, p4, p5)

# call function

x1 = func_1(1,2,3,4,5)   # OK all arguments
try:
    x2 = func_1(1,2,3,4)     # TypeError: func_1() missing 1 required positional argument: 'p5'
except:
    print('TypeError: func_1() missing 1 required positional argument: \'p5\'')

y1 = func_2(1,2,3,4,5)
print('y1 = func_2(1,2,3,4,5): ', y1) # (1, 2, 3, 4, 5)


print('\n# 2. Functions def args - defaults\n')

def func_2(p1, p2 = 2, p3 = 3, p4 = 4, p5 = 5): # only first argument is required and return tuple of arguments
    return (p1, p2, p3, p4, p5)

# call

z1 = func_2(10,20,30,40,50)
print('z1 = func_2(10,20,30,40,50): ', z1)  #  (10, 20, 30, 40, 50)

z2 = func_2(10)
print('z2 = func_2(10): ', z2)              # (10, 2, 3, 4, 5)


print('\n# 3. Functions def *args\n')

def func_args(*args):   # don't know how many args
    print(*args)

list = [1,2,3,4,5]
n1, n2, *n = list
print('n1:', n1)        # 1
print('n2:', n2)        # 2
print('*n:', *n)        # 3 4 5
print(list)             # [1, 2, 3, 4, 5]
print(*list)            # 1 2 3 4 5
print(*list,sep='-')    # 1-2-3-4-5


print('\n# 4. Functions def *kwargs\n')

def func_3(*args, **kwargs):  # convention args and kwargs
    print('args  : ', args)
    print('kwargs: ', kwargs)
    if kwargs.get('kwarg1'):
        kwarg1 = kwargs['kwarg1']
    else:
        kwarg1 = None
    if kwargs.get('kwarg2'):
        kwarg2 = kwargs['kwarg2']
    else:
        kwarg2 = None
    if kwargs.get('kwarg3'):
        kwarg3 = kwargs['kwarg3']
    else:
        kwarg3 = None
    if kwargs.get('kwarg4'):
        kwarg4 = kwargs['kwarg4']   # if not defined cant be found -> KeyError: 'kwarg4'
    else:
        kwarg4 = None
    print('kwarg1: ', kwarg1)
    print('kwarg2: ', kwarg2)
    print('kwarg3: ', kwarg3)
    print('kwarg4: ', kwarg4)


# call

func_3(1, '2', True, 'three', kwarg1='kwarg1', kwarg2 = 'kwarg2', kwarg3 = 'kwarg3', qualquercoisa='qualquer conteudo')
    # args  :  (1, '2', True, 'three')
    # kwargs:  {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2', 'kwarg3': 'kwarg3', 'qualquercoisa': 'qualquer conteudo'}

