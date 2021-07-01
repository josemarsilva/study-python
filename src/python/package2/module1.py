#
# filename   : ./package2/module1.py
# Description: Packages, modules, relative references, sys.path
# Docs       :
#
from src.python import package2

var_pck2_mod1 = 'package2.module1.var'
var_same_name = var_pck2_mod1

# base reference 'src.python.package1.module1' is necessary to import modules upper than __main__
# Python, by default, don't see nothing above current __main__
import src.python.package1.module1 as module1
var_imp_pck1_mod1 = module1.var_pck1_mod1

print('')
print('./package2/module1.py')
print(f'(var_pck2_mod1,var_same_name): ({var_pck2_mod1},{var_same_name})')
print(f'(var_imp_pck1_mod1)          : {var_imp_pck1_mod1}')
print('')

