#!/home/jepoy/anaconda3/bin/python

# in python functions and procedures are same

def main():
    x = kitten(5)
    print(x)

def kitten(n):
    print(f"{n} Meow.")
    # This function does not have a return
    # that's why it returns None
    # if it had return value then it would equal that value

if __name__ == '__main__':
    main()