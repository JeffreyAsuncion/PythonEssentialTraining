#!/home/jepoy/anaconda3/bin/python

def main():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # game.append('Computer') # tuples are immutable 
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': 
    main()