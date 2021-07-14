from colorsys import hsv_to_rgb

rs = 1000 # rectangle size
angle = 0 # angle (we will augment this )
pages = 36 # the number of pages to draw

# let’s manage our colors
hue = 0 # goes through the rainbow, start with red
sat = 1 # goes from white to bright
val = 1 # goes from black to bright

# how many squares are we drawing towards the center
squareCount = 116

# loop through the pages
for page in range(pages):
    # code at this indent will run once per page!
    # make a new page and set its frame duration
    # 1 = 1 second!
    newPage(1000, 1000)
    frameDuration(1/15)

    # draw a gray background sqare that fills the whole canvas
    fill(.25)
    rect(0, 0, width(), height())

    # move our (0, 0) to the middle of the canvas
    translate(width()/2, height()/2)

    # loop through
    for i in range(squareCount):
        # the code at this indent will be run once per square
        # i will be equal to each number as we loop through the squares (0, 1, 2, 3, 4, 5)
        # we will use this to determine whether the square is odd or even

        # we will use the modulo to test if the number is odd or even
        # i % 2 == 0: no remainder, the number is even
        # i % 2 == 1: remainder, the number is odd
        if i % 2:
            # if the number is odd, run the code at this indent
            # use hsv_to_rgb() to convert our hue, sat, val to RGB
            # use the asterisk to “unpack” the tuple provided to us from hsv_to_rgb()
            fill(*hsv_to_rgb(hue, sat, val))
        else:
            # if the number is even, just set the fill to black
            fill(0)
        
        # every time we go through the hue, augment it
        # by dividing it by the number we are looping through
        # we will go from 0 to 1 as we progress through the loop
        hue += 1/squareCount
        
        # now we finally draw our rectangle
        rect(-rs/2, -rs/2, rs, rs)
        
        # once we’ve drawn our rectangle
        # we can manipulate the scale and rotation of the canvas 
        # everything from now on will be drawn with these dimensions
        scale(.95)
        rotate(angle)

    # augment the angle by one “slice of pie” (360 is the whole pie, and our animation will document one full 360° rotation)
    # use the += shortcut, which is the same as typing
    # angle = angle + 360/pages
    angle += 360/pages

# save the resulting image as an animated gif
saveImage('fancySpiral.gif')