#!/home/jepoy/anaconda3/bin/python

# read up on build-in string functions

class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'



x = bunny(47)
print(repr(x))
print(x)
print(ascii(x))  # will only use ascii character no emoji or special chars   
print(chr(128406))
print(ord('🖖'))