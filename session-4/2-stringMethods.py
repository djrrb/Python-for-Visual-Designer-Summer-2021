def divider():
    print('='*20)

print('1. define a string:')
s = 'hello world'
print(s)
divider()

print('2. select a character by index:')
print('first:', s[0])
print('third:', s[2]) 
print('last:', s[-1])
divider()

print('3. select a slice:')
print('first two chars:', s[:2])
print('last three chars:', s[-3:])
divider()

print('4. append to string:')
s += " it’s me"
print(s)
divider()

print('5. change case of string:')
print(s.upper())
print(s.lower())
print(s.title())
divider()

print('6. replace:')
s = s.replace('world', 'planet')
print(s)
divider()

print('7. test for inclusion:')
print('hello', 'hello' in s)
print('goodbye', 'goodbye' in s)

divider()
print('8. use a string to join a list together')
print(', '.join(['apples', 'oranges', 'bananas']))

divider()
print('9. split a string into a list of parts')
print('for example, split by wordspace:')
print(s.split(' '))
