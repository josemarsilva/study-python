#
# filename   : usercustompackage/__init__.py
# Description: Provide some calculation functions
# Docs       :  *
#

print('\n#1. Modulue import - calculate\n')

from calculate import calc_price, calc_tax
from subpackage.fmt import format_value, format_percentual

vlr_cost = 100.00
pct_markup = 40/100  # 40%
vlr_price = calc_price(vlr_cost, pct_markup)
vlr_tax_price = calc_tax(vlr_price)

print(f'vlr_cost      : {vlr_cost}')
print(f'pct_markup    : {pct_markup}')
print(f'vlr_price     : {vlr_price}')
print(f'vlr_tax_price : {vlr_tax_price}')
print('')
print(f'format_value(vlr_cost)              : {format_value(vlr_cost)}')
print(f'format_format_percentual(pct_markup): {format_percentual(pct_markup)}')
print(f'format_value(vlr_price)             : {format_value(vlr_price)}')
print(f'format_value(vlr_tax_price)         : {format_value(vlr_tax_price)}')

