# in this script, we will use loops to make a grid of shapes

# Anatomy of a loop:
    # for = python keyword for loop
    # x = variable name, can be anything. the value of this variable will change every time we run the block of code.
    # in = connects us to the sequence we will loop through
    # range(0, 10) = use the range() function to get a sequence of numbers. range takes (start, end, step)

# loop through the rows
# the y variable will start at 0 and increase by 100 each time until it hits 1000
for y in range(0, 1000, 100):
    # loop through the columns
    # the x variable will start at 0 and increase by 100 each time until it hits 1000
    for x in range(0, 1000, 100): 
        print(x)
        # fill: red, green, blue, alpha/transparency
        # each is between 0 and 1
        fill(random(), random(), random(), 1)
        # could also do cymkFill()
        # cmykFill: cyan, magenta, yellow, black, alpha
        #cmykFill(1, 0, 0, 1)
        
        # draw a shape, could be a rectangle or an oval
        # x, y, width, height
        oval(x, y, 100, 100)
        
        # this is the end of our column block which runs 100 times
    # this is the end of our row block, which runs 10 times
# now have exited both loops and all the code that follows will run once

# save our image in various formats, if we want
saveImage('grid.gif')
saveImage('grid.pdf')
saveImage('grid.png')