#
# filename   : usercustompackage/calculate.py
# Description: Provide some functions to package usercustompackage
# Docs       :  *
#

PCT_TAX_DEFAULT = 0.20 # 20 %

def calc_price(value, pct_markup):
    return value * (1 + pct_markup)

def calc_tax(value):
    return value * PCT_TAX_DEFAULT

