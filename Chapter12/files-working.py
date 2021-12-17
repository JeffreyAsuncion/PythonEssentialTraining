#!/home/jepoy/anaconda3/bin/python

def main():
    f = open('lines.txt', 'r')   # 'w' write - rewrites over the file # a append add to the end of the file
    for line in f:
        print(line.rstrip())
    f.close()

if __name__ == '__main__':
    main()