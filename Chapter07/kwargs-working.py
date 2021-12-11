#!/home/jepoy/anaconda3/bin/python

def main():
    kitten(Buffy = 'meow', Zilla = 'grrr', Angel = 'purr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')

if __name__ == '__main__':
    main()