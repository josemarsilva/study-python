#
# filename   : aula-105-variable-scopes-global-function-local.py
# Description: variable scopes: global vs function local
# Docs       : https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#

print('\n# 1. Variable Scopes: Global vs Function(local)\n')

variable = 'global'
global_var_changeble = 0

def print_variable():
    print('print_variable().variable: ', variable)
    print('print_variable().globa_var_changeble: ', global_var_changeble)

def change_variable():
    variable = 'local'  # only local scope variable was changed!
    global global_var_changeble
    global_var_changeble = 1
    print('change_variable().variable: ', variable)
    print('global.globa_var_changeble: ', global_var_changeble)


#  call

print_variable()
                    #print_variable().variable:  global
                    #print_variable().globa_var_changeble:  0

change_variable()
                    # change_variable().variable:  local
                    # global.globa_var_changeble:  1

print('variable            : ', variable)               # variable            :  global
print('global_var_changeble: ', global_var_changeble)   # global_var_changeble:  1
