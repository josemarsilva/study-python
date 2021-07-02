#
# filename   :
# Description: Solving mutable arguments function
# Docs       :  * https://docs.python.org/3.9/reference/index.html
#

print(f'\n#1. Solving mutable arguments function - Problem\n')

# MUTABLES: List and Dictionaries
# IMUTABLES: Tuplas, strings, numbers, boolean, None

def list_customers(customer_iterable, list_init=[]):
    list_init.extend(customer_iterable)
    return list_init

customers1 = list_customers(['Jose', 'Maria', 'Joao', 'Pedro'])
customers2 = list_customers(['Paulo', 'Marcus', 'Jonas', 'Isais'])

print(f'customers1: {customers1}')  # ['Jose', 'Maria', 'Joao', 'Pedro', 'Paulo', 'Marcus', 'Jonas', 'Isais']
print(f'customers1: {customers2}')  # ['Jose', 'Maria', 'Joao', 'Pedro', 'Paulo', 'Marcus', 'Jonas', 'Isais']

# Undesired behavior: both lists customers1 and customers2 has all date
# The expected was:
# * customers1 = ['Jose', 'Maria', 'Joao', 'Pedro']
# * customers2 = ['Paulo', 'Marcus', 'Jonas', 'Isais']

print(f'\n#2. Solving mutable arguments function - Solution\n')

def list_customers(customer_iterable, list_init=None):
    if list_init is None:
        list_init = []
    list_init.extend(customer_iterable)
    return list_init

customers1 = list_customers(['Jose', 'Maria', 'Joao', 'Pedro'])
customers2 = list_customers(['Paulo', 'Marcus', 'Jonas', 'Isais'])

print(f'customers1: {customers1}')  # ['Jose', 'Maria', 'Joao', 'Pedro', 'Paulo', 'Marcus', 'Jonas', 'Isais']
print(f'customers1: {customers2}')  # ['Jose', 'Maria', 'Joao', 'Pedro', 'Paulo', 'Marcus', 'Jonas', 'Isais']

