# create a variable for the offset of a fake z axis
zOffset = 0
# create a variable for the offset of the shape size
sizeOffset = 0
# these both start at zero, but in the loop we will change their values

# z represents the fake depth we will get by stacking grids on top of one another offset by a certain amount

rect(0, 0, width(), height())

for z in range(11):
    # now do our grid loops for y and x
    for y in range(0, width(), 100):    
        fill(random(), random(), random())
        for x in range(0, width(), 100):    
            # draw the oval, but instead of just using x and y, add the zOffset and sizeOffset variables so that the position and dimensions will change
            oval(x+zOffset, y+zOffset, 50+sizeOffset, 50+sizeOffset)
    # dedent all the way out to the z loop
    # now we can shift the position of the next grid
    # and tell it to draw the shapes smaller
    zOffset = zOffset + 8
    sizeOffset = sizeOffset - 3

saveImage('cones.png')