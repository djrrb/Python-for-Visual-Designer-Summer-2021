def myShape(sh=200):
    
    # handle starting length
    hsl = 130
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



fill(random(), random(), random(), .2)

shapeHeight = 100
for i in range(10):
    myShape(shapeHeight)
    shapeHeight += 100