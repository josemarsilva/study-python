#
# filename   : lab-17-string-index-slice.py
# Description: String [index], slice [start:end]
# Docs       : https://docs.python.org/3/whatsnew/2.3.html#extended-slices
#

#           0         1          2
#           0123456789001234567890
str_text = "Python e charmoso"

print(str_text[2])      # t
print(str_text[0:2])    # Py
print(str_text[9:13])   # charm

print(str_text[-1])     # o
print(str_text[-2])     # s
print(str_text[-8:-3])  # oso

print(str_text[0:5:2])  # Pto

print(str_text.__len__())   # 17
print(len(str_text))        # 17

