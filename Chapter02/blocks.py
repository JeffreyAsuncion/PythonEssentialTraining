#!/usr/bin/env python3

x = 42
y = 73


# Python has no Switch or Case Statement
# Python uses the if elif ... else blocks

if x > y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print('do something else')
