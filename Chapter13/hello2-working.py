#!/home/jepoy/anaconda3/bin/python

# read up on build-in container functions


x = ( 1, 2, 3, 4, 5)
y = x
print(x)
print(y)
print()

x = ( 1, 2, 3, 4, 5)
y = len(x)
print(x)
print(y)
print()

x = ( 1, 2, 3, 4, 5)
y = list(reversed(x)) # reversed returns an object, need to use list 
print(x)
print(y)
print()

x = ( 1, 2, 3, 4, 5)
y = sum(x)  # try max() and min() 
print(x)
print(y)
print()

x = ( 0,0,0,0,0) # try (0,0,0,1,0)
y = any(x)  # boolean function try all(),
print(x)
print(y)
print()

x = ( 1, 2, 3, 4, 5)
y = ( 6, 7, 8, 9, 10) 
z = zip( x, y ) # z returns an iterator
for a, b in z:
    print(f' {a} --- {b}')
print()


x = ( 'cat', 'dog', 'rabbit', 'velociraptor' )
for i, v in enumerate(x):
    print(f'{i} ---- {v}')
print()

