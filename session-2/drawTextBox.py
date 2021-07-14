from random import shuffle

fs = 90

# define our text as a string
myString = 'hello world'
# we can add to it and also use \n for new lines
myString += '\n' + 'this is a new line'

myString += """
we can also
use multiline
strings
"""

# draw a grey rectanle
fill(.5)
rect(100, 100, 700, 700)

fontSize(fs)
font('Georgia')
fill(1)
# if we define tracking relative to font size
# it will always be proportional to it
tracking(-20/fs)
# same thing with line height
lineHeight(1.2*fs)
# gah make a quote
stroke(0, 1, 0)

# text box takes two things:
# the string that we will draw
# the rectangle that the text will wrap in
# (x, y, width, height)
textBox(myString, (100, 100, 700, 700))