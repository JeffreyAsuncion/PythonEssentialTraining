#!/home/jepoy/anaconda3/bin/python


x = [ '-', '-', 'X', 'X' ]
# x.pop()
x.insert(0, x.pop(-1))
print(x)
