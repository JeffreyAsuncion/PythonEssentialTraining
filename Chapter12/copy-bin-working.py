#!/home/jepoy/anaconda3/bin/python

def main():
    infile = open('berlin.jpg', 'rb') # read bit
    outfile = open('berlin-copy.jpg', 'wb') # write bit
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()