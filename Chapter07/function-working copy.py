#!/home/jepoy/anaconda3/bin/python

# in python functions and procedures are same

def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print("Meow.")
    return 42

if __name__ == '__main__':
    main()