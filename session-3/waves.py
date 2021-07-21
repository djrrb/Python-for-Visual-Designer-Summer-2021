# define a function that is a shape
def myShape(sh):
    # handle starting length
    hsl = 950
    # get the right and left handle lengths
    rightHandleLength = randint(-hsl, hsl)
    leftHandleLength = randint(-hsl, hsl)
    # define a bezier path
    bp = BezierPath()
    # move to my starting point
    bp.moveTo((0, 0))
    # straight line across
    bp.lineTo((width(), 0))
    # straight line up
    bp.lineTo((width(), sh))
    # make my curve
    bp.curveTo(
        (width(), sh+rightHandleLength), #handle on right
        (0, sh-leftHandleLength), #handle on left
        (0, sh) # left corner point
        )
    drawPath(bp)

# this background function makes 10 shapes at different heights
def drawBackground():
    # define a shape height
    sh = 200
    # loop 10 times
    for i in range(10):
        # set a random semi-transparent color
        fill(random(), random(), random(), .2)
        # draw the shape
        myShape(sh)
        # next time, make the shape 100 units taller
        sh += 100

# make a new page and draw the background
newPage('Letter')
drawBackground()
