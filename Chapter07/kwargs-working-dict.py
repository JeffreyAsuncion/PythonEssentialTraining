#!/home/jepoy/anaconda3/bin/python

def main():
    x = dict(Buffy = 'meow', Zilla = 'grrr', Angel = 'purr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')

if __name__ == '__main__':
    main()