#!/home/jepoy/anaconda3/bin/python

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v)) # note *v - returns a collection
    v = sys.platform
    print(v)
    v = os.name
    print(v)
    v = os.getenv('PATH')
    print(v)
    v = os.getcwd() # Current Working Directory
    print(v)
    v = os.urandom(25) # btye object
    print(v)
    x = random.randint(1, 1000)
    print(x)

    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    now =  datetime.datetime.now()
    print(now, now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


if __name__ == '__main__': main()