#
# filename   : ./package1/module2.py
# Description: Packages, modules, relative references, sys.path
# Docs       :
#

var_pck1_mod2 = 'package1.module2.var'
var_same_name = var_pck1_mod2

import module1
var_imp_pck1_mod1 = module1.var_pck1_mod1

print('')
print('./package1/module1.py')
print(f'(var_pck1_mod2,var_same_name): ({var_pck1_mod2},{var_same_name})')
print(f'(var_imp_pck1_mod1)          : {var_imp_pck1_mod1}')
print('')

