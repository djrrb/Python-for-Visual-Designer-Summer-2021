names = """betty
Rian
Rahel
Muhammad
Sarah"""

nameList = names.split('\n')
from random import shuffle
shuffle(nameList)
print('\n'.join(nameList))
