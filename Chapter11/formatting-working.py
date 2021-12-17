#!/home/jepoy/anaconda3/bin/python

x = 42
y = 73
print('the number is {} {}'.format(x, y))

# keyword agruments
print('the number is {xx} {bb}'.format(bb = x, xx = y))

# positional arguments
print('the number is {0} {1} {0}'.format(x, y))

# adding formatting instructions
print('the number is {0:<05} {1:>05}'.format(x, y))
z = 42 * 747 * 1000
print('the number is {:,}'.format(z))
print('the number is {:,}'.format(z).replace(',','.'))
print('the number is {:.3f}'.format(z))


x = 42
# hexadecimal
print('the number is {:x}'.format(x))
# octal
print('the number is {:o}'.format(x))
# binary
print('the number is {:b}'.format(x))


# starting with python 3.6 
# the introduction of the fstring
# f''

print(f'the number is {x} {y}')
