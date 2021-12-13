#!/home/jepoy/anaconda3/bin/python

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1:5:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Computer')
    print(', '.join(game))
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': 
    main()