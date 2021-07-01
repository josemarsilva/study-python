#
# filename   : lab-126-package-module-relative-reference-sys-path.py
# Description: Packages, modules, relative references, sys.path
# Docs       :  * https://docs.python.org/3.9/reference/index.html
#

print('\n#1. Packages and modules: relative references\n')

print('+ package1:')
print('  - module1:')
print('    * var = \'package1.module1.var\'')
print('  - module2:')
print('    * var = \'package1.module2.var\'')
print('+ package2:')
print('  - module1:')
print('    * var = \'package2.module1.var\'')
print('+ package3:')
print('  + subpackage31:')
print('    - module1:')
print('      * var = \'package3.subpackage31.module1.var\'')


print('\n#2. Packages and modules: sys.path\n')

import sys
print(f'sys.path: {sys.path}') # sys.path: ['C:\\GitHome\\ws-github-06\\study-python\\src\\python', 'C:\\GitHome\\ws-github-06\\study-python', 'C:\\GitHome\\ws-github-06\\study-python\\venv\\Scripts\\python36.zip', 'C:\\Program Files\\Python36\\DLLs', 'C:\\Program Files\\Python36\\lib', 'C:\\Program Files\\Python36', 'C:\\GitHome\\ws-github-06\\study-python\\venv', 'C:\\GitHome\\ws-github-06\\study-python\\venv\\lib\\site-packages']


print('\n#3. Packages and modules: Import Package1 Module1\n')

import package1.module1


print('\n#3. Packages and modules: Import Package1 Module2 and Package2 Module1 \n')

try:
    import package1.module2
except ModuleNotFoundError:
    print('ERROR: import package1.module2 causes ModuleNotFoundError')
    print('       ./package1/module2.py in line 10 references to "import module1" using current sys.path')
    print('           :')
    print('         import module1')
    print('           :')
