#
# filename   : lab-11-logical-operator.py
# Description: Logical operators: and, or, not, in, not in
# Docs       : https://docs.python.org/3/contents.html
#

a = 2
b = 2
c = 3
str_1 = "a"
str_2 = "abcdefghijklmnopqrstuvxwyz"
str_3 = "1"

# and
if a == b and b < c:
    print("verdade")
else:
    print("false")

# or
if a == b or b == c :
    print("verdade")
else:
    print("false")

# not
if not a == b:
    print("verdade")
else:
    print("false")

# in
if str_1 in str_2:
    print("verdade")
else:
    print("false")

# not in
if str_1 not in str_2:
    print("verdade")
else:
    print("false")
