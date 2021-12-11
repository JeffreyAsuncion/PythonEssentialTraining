#!/home/jepoy/anaconda3/bin/python

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog':
        continue # it will skip printing dog and continue loop
    # if pet == 'velociraptor':
    #     break
    print(pet)
else:
    print('that is all of the animals')
