# a saved state example

# set some constants
cols, rows = 8, 8
cellWidth, cellHeight = 115, 115
shapeWidth, shapeHeight = 80, 80

with savedState():
    # draw a title in the top left
    fill(0, 1, 1)
    translate(0, height()-50)
    fontSize(50)
    text('here is my grid', (0, 0))
    # but don’t bother remembering any of these settings
    
# we are now back in the bottom left corner
# loop through row indexes
# y = 0, 1, 2, 3...
for y in range(rows):
    # loop through column indexes
    # x = 0, 1, 2, 3...    
    for x in range(cols):
        # save our state
        # (0, 0) will be at the bottom left at this indent
        with savedState():
            # if we are on the first row
            # make it red
            if x == 0:
                fill(1, 0, 0)
            # move our (0, 0) to the point where we will draw the shape
            # only within the saved state
            translate(x*cellWidth, y*cellHeight)
            # make another saved state
            with savedState():
                # do some temporary rotation and translation to draw the shape from the center
                #and then move back
                translate(cellWidth/2, cellHeight/2)
                rotate(45)
                stroke(.5)
                strokeWidth(8)
                rect(-shapeWidth/2, -shapeHeight/2, shapeWidth, shapeHeight)
            # draw some text too 
            # no more stroke and rotation
            fill(1)
            fontSize(100)
            text('A', (24, 20))
        # move back to bottom left