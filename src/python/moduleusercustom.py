#
# filename   : moduleusercustom.py
# Description: User Custom module
# Docs       :
#

# Python does not have constants! Convention for constants is UPPERCASE

MODULE_NAME = 'USER CUSTOM'
VERSION = '2021.06.30'
COTACAO_DOLAR = 5.15
PI_VALUE = 3.1415

def hello():
    print('hello world! ')
    # return None (is default)

def goodbye():
    print('good bye! ')
    # return None (is default)


if __name__ == '__main__':
    print('__name__     : ', __name__)
    print('MODULE_NAME  : ', MODULE_NAME)
    print('VERSION      : ', VERSION)
    print('COTACAO_DOLAR: ', COTACAO_DOLAR)
    print('PI_VALUE     : ', PI_VALUE)
