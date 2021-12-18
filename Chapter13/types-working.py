#!/home/jepoy/anaconda3/bin/python


# read up on build-in numeric functions

x = '47'
y = int(x) # not a function but a constructor for the int type
z = float(x)

print(f'x is {type(x)}')
print(f'x is {(x)}')
print(f'x is {type(y)}')
print(f'x is {(y)}')
print(f'x is {type(z)}')
print(f'x is {(z)}')

x = -47
y = abs(x)
print(f'x is {type(x)}')
print(f'x is {(x)}')
print(f'x is {type(y)}')
print(f'x is {(y)}')

x = 47
y = divmod(x, 3)
print(f'x is {type(x)}')
print(f'x is {(x)}')
print(f'x is {type(y)}')
print(f'x is {(y)}')

x = 47
y = x + 73j
print(f'x is {type(x)}')
print(f'x is {(x)}')
print(f'x is {type(y)}')
print(f'x is {(y)}')

x = 47
y = complex(x, 73)
print(f'x is {type(x)}')
print(f'x is {(x)}')
print(f'x is {type(y)}')
print(f'x is {(y)}')