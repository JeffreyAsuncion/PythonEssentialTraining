#!/home/jepoy/anaconda3/bin/python

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if a or b:
    print('expression is true')
else:
    print('expression is false')

if y in x:
    print('expression is true')
else:
    print('expression is false')