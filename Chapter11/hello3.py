#!/home/jepoy/anaconda3/bin/python

print('Hello, World.')

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World.'.casefold())

s1 = 'Hello, World.'
s2 = s1.upper()

print(id(s1))
print(id(s2))

s1 = 'Hello, World.'
s2 = 'this is another string'

print(s1 + ' ' + s2)

s3 = " this " " that "   # another way to concatenate strings

print(s3)






