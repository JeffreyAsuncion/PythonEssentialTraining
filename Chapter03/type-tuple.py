
x = ( 1, 'two', 3.0, [4, 'four'], 5 )
y = ( 1, 'two', 3.0, [4, 'four'], 5 )

print('x is {}'.format(x))
print(type(x), id(x))
print(type(y), id(y))

if x[0] is y[0]: 
    print("yep")
else:
    print("nope")


y = [ 1, 'two', 3.0, [4, 'four'], 5 ]

# test for x and y 
if isinstance(y, tuple):
    print("tuple")
elif isinstance(y, list):
    print("list")
else:
    print("nope")