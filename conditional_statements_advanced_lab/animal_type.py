# Input: name of an animal
animal = input()

# Lists of animals grouped by their biological class
mammals = ['dog']
reptiles = ['crocodile', 'tortoise', 'snake']

# Check the animal type and print the classification
if animal in mammals:
    print('mammal')
elif animal in reptiles:
    print('reptile')
else:
    print('unknown')
