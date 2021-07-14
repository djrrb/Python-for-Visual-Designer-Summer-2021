# a simple spiral

rs = 1000 # rectangle size
angle = 0 # starting angle
pages = 10 # number pages

# loop through pages
for page in range(pages):
    # make a new page
    newPage(1000, 1000)
    # set it’s animation duration
    frameDuration(1/15)

    # give us a dark grey background
    fill(.25)
    rect(0, 0, width(), height())

    # move to the center
    translate(width()/2, height()/2)

    # set our fill to None
    # this a special keyword that starts with a capital N
    fill(None)
    
    # make the stroke a lovely blue
    # using RGB values divided by 255
    stroke(62/255, 184/255, 204/255)
    # define the stroke thickness
    strokeWidth(10)

    # loop a number of times
    for i in range(50):
        # print the current instance of our loop
        print(i)
        # draw a rectangle
        # to draw it from the center, subtract half the width and height from the x, y position
        rect(-rs/2, -rs/2, rs, rs)
        # make the canvas a little smaller and rotate
        scale(.9)
        rotate(angle)
    #angle = angle + 10
    angle += 1

# save the image, if we want
saveImage('spiral_simple.gif')