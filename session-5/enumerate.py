# the enumerate function is handy
# it converts a sequence of items into a sequence of tuples that pair the index number with the item

myList = ['apples', 'bananas', 'oranges']

# this is one way of keeping track of where we are in a list
count = 0
for item in myList:
    print(item, count)
    count += 1

# 
print(list(enumerate(myList)))

# this is the same as the code above, but the count variable is defined already rather than having to set it up and establish it ourselves
for count, item in enumerate(myList):
    print(item, count)