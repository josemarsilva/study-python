#
# filename   : lab-122-module-import-library-usercustom-pip-install-venv-activate.py
# Description: Module import, default library, user custom library, pip install, venv activate
# Docs       :  * https://docs.python.org/3/py-modindex.html
#

print('\n#1. Python Modules\n')


print('\n#2. Python Modules - Documentation of all standard modules\n')

print('* here you can see all default installed modules')
print('  https://docs.python.org/3/py-modindex.html')
print('* here you can see a lot of packages of Python Community')
print('  https://pypi.org/')

print('\n#2. Python Modules - Use PIP and VENV to install new ones\n')

print('* remember to use venv to manage different enviromnet')
print('* use pip install to install custom module')

# next import use pymysql that is not default installed - that is a problem
try:
    import pymysql  # ModuleNotFoundError: No module named 'pymysql'
except:
    print('')
    print('# you can use pip install pymysq to solve problem')
    print('# + run command (to activate venv enviroment):')
    print('#   C:\...\study-python> venv\Scripts\\activate')
    print('# + run command (to install pymysql):')
    print('#   C:\...\study-python> pip install pymysql')
    print('#   +-------------------------------------------------------------------------------------------------+')
    print('#   | Collecting pymysql                                                                              |')
    print('#   |   Downloading https://files.pythonhosted.org/packages/.../PyMySQL-1.0.2-py3-none-any.whl (43kB) |')
    print('#   |      100% |████████████████████████████████| 51kB 1.5MB/s                                       |')
    print('#   |  Installing collected packages: pymysql                                                         |')
    print('#   |  Successfully installed pymysql-1.0.2                                                           |')
    print('#   |  You are using pip version 10.0.1, however version 21.1.3 is available.                         |')
    print('#   |  You should consider upgrading via the python -m pip install --upgrade pip command.             |')
    print('#   +-------------------------------------------------------------------------------------------------+')


print('\n#3. Python Modules - Import user custom module and use imported things\n')

# * there is a file 'moduleusercustom.py' in the same directory
# * do not use extensin '.py'
# * special characters in name like spaces, separator, etc requires aditional force :-)

# from moduleusercustom import hello, goodbye, MODULE_NAME, PI, VERSION

from moduleusercustom import MODULE_NAME, VERSION, COTACAO_DOLAR, PI_VALUE, hello, goodbye
# Optionally you can import all module, not each objects inside
# import moduleusercustom

print(f'MODULE_NAME  : {MODULE_NAME}')
print(f'VERSION      : {VERSION}')
print(f'COTACAO_DOLAR: {COTACAO_DOLAR}')
print(f'PI_VALUE     : {PI_VALUE}')

print('')
hello()    # call function inside module imported
goodbye()
print('')


print('\n#4. Python Modules - Import user custom module name-dash-name-dash using importlib\n')

import importlib
map_data = importlib.import_module("lab-117-map-data")

print(f'map_data.products : {map_data.products}')
print(f'map_data.customers: {map_data.customers}')
print(f'map_data.list_nums: {map_data.list_nums}')
