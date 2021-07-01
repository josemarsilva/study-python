#
# filename   : usercustompackage/subpackage/fmt.py
# Description: provides function format_value()
# Docs       :  *
#

def format_value(value):
    return f'R$ {value:.2f}'

def format_percentual(pct):
    return f'{pct*100:.1f}' + '%'
