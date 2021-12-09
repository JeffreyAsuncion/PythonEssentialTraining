#!/home/jepoy/anaconda3/bin/python


# Python has Duck Typing - Walks like  a Duck

x = 7 
print('x is {}'.format(x))
print(type(x))

x = 'seven'.capitalize()
print('x is {}'.format(x))
print(type(x))

x = 'seven "{1:<09}" "{0:>9}"'.format(8, 9)
print('x is {}'.format(x))
print(type(x))

a = 8
b = 9
x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))

x = 7 / 3
print('x is {}'.format(x))
print(type(x))

x = 7 * 3.141592
print('x is {}'.format(x))
print(type(x))

x = .1 + .1 + .1 - .3
print('x is {}'.format(x))
print(type(x))


from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))