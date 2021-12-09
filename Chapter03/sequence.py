#!/home/jepoy/anaconda3/bin/python

# for a list, mutable

x = [ 1, 2, 3, 4, 5 ]

x[2] = 42   # item at index 2 is reassigned  

for i in x:
    print('i is {}'.format(i))

print("@"*20)

# for a tuple, immutable

x = ( 1, 2, 3, 4, 5 )
# this will throw an exception 
# x[2] = 42   # item at index 2 is reassigned  
for i in x:
    print('i is {}'.format(i))

print("@"*20)

# for a range

x = range(5)    # note [0, 1, 2, 3, 4]
for i in x:
    print('i is {}'.format(i))

print("@"*20)

# for a dictionary, mutable

x = { 'one': 1, 'two': 2, 'three': 3, 'four' :  4, 'five' : 5 }

x['three'] = 42

for key, value in x.items():
    print('k: {}, v: {}'.format(key, value))

