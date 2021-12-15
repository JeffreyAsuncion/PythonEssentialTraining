#!/home/jepoy/anaconda3/bin/python

import sys

def main():
    # print('Hello, World.')
    try:
        # x = int('foo')  # read error msg 'Traceback'
        x = 5 / 0
    except ValueError:
        print("I caught a ValueError")
    # except ZeroDivisionError:
    #     print("don't divide by zero")
    except:
        print(f"unknown error: {sys.exc_info()}")
    else:
        print('good job!')
        print(x)


if __name__ == '__main__': 
    main()