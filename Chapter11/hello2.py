#!/home/jepoy/anaconda3/bin/python

class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello, World.')
print(s)