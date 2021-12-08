#!/usr/bin/env python3
#!/home/jepoy/anaconda3/bin/python
## at terminal which python

class Duck:
    sound = 'Quaaack!!!'
    walking = 'Walking like a duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()