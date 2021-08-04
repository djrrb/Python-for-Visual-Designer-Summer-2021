myList = ['apples', 'bananas', 'oranges']

count = 0
for item in myList:
    print(item, count)
    count += 1
    
print(list(enumerate(myList)))

for count, item in enumerate(myList):
    print(item, count)