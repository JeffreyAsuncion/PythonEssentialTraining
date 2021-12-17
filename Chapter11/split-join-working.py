#!/home/jepoy/anaconda3/bin/python

s = 'This is a long string with a bunch of words in it.'
print(s)
print(s.split())  # will split on the ' '

l = s.split()
s2 = ':'.join(l)
print(s2)


