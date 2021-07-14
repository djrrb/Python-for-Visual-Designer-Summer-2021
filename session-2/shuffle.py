# import the shuffle function from the random module
# https://docs.python.org/3/library/random.html

from random import shuffle
# define a string
myString = 'hello world'
# convert it to a list
# (for whatever reason we can only shuffle lists)
myList = list(myString)
# shuffle it
shuffle(myList)
# convert the list back to a string joined by whatever is in between the quotes
print('_'.join(myList))