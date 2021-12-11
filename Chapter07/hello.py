#!/home/jepoy/anaconda3/bin/python

def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

@f1
def f3():
    print('this is f3')

f3()