# copy names out of a spreadsheet
# it's a multiline string, so use three quotes
names = """betty
Rian
Rahel
Muhammad
Sarah"""

# convert the names into a proper python list by splitting it by the newline character (\n)
nameList = names.split('\n')
# from the random python library import the shuffle function so we can use it in this script
from random import shuffle
# use shuffle() randomize the order of items in the list
shuffle(nameList)
# join the list together into a string with \n, so we see each name on a separate line
print('\n'.join(nameList))
