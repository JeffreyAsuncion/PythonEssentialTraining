#!/home/jepoy/anaconda3/bin/python

def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        # this way strips the right white spaces
        # print(line.rstrip(), file=outfile) # same as below
        outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__':
    main()