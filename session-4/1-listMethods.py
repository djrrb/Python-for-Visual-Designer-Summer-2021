def divider():
    print('='*20)
print('1. define a list:')
x = ['apples', 'oranges', 'bananas', 'peaches']
print(x)
divider()

print('2. select an item by index:')
print('first item:', x[0])
print('third item:', x[2]) 
print('last item:', x[-1])
divider()

print('3. select a slice of the list:')
print('first two items:', x[:2])
print('last three items:', x[-3:])
divider()

print('4. append an item to a list:')
x.append('cherries')
print(x)
divider()

print('5. delete an item from the list:')
del x[3]
print(x)
divider()

print('6. reverse the order of a list:')
x.reverse()
print(x)
divider()

print('7. merge two lists')
x += ['strawberries', 'blueberries']
print(x)
divider()

print('8. sort alphabetically / numerically:')
x.sort()
print(x)
divider()

print('9. test for membership')
print('bananas', 'bananas' in x)
print('grapefruit', 'grapefruit' in x)