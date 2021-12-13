#!/home/jepoy/anaconda3/bin/python

def main():
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'loin': 'grrr',
    #     'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    animals = dict( kitten = 'meow', puppy = 'ruff!',  loin = 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    for k in animals.keys():
        print(k)
    for v in animals.values():
        print(v)
    animals['loin'] = 'I am a loin'
    animals['monkey'] = 'Ah kunamatata'
    # print(animals['godzilla']) # this will cause and error if the key is not present
    print(animals.get('godzilla'))
    print_dict(animals)
    print('loin' in animals)

def print_dict(o):
    for key, value in o.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()