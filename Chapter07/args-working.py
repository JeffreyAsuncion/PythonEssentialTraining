#!/home/jepoy/anaconda3/bin/python

def main():
    kitten('meow', 'grrr', 'purr')

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')

if __name__ == '__main__':
    main()