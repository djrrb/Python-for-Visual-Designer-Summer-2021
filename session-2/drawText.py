myText = 'hello world'

fontSize(160)
font('Georgia')
fill(1, 0, 0)
stroke(0, 1, 0)
tracking(-10)

# give us a little margin
translate(100, 100)

# text() takes two things
# the string we will draw
# the x, y coordinates to start at
text(myText, (0, 0))