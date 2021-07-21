newPage(700, 970)
mySize = 130
# make a formatted string
fs = FormattedString('hello world', font='MinionPro-Regular', fontSize=mySize)
# make a bezier path
bp = BezierPath()
# feed the text into the bezierPath
bp.text(fs)
# draw the original text up top
translate(50, height()-mySize)
drawPath(bp)

# loop a few times
# augment v, the variance of the points from the original
for v in range(1, 12, 2):
    # make a second bezier path
    bp2 = BezierPath()
    # loop through the first bezier path
    # and draw into the second bezier path
    # EXCEPT, randomize the points by v 
    # before we draw into the second
    
    # loop through contours
    for ci, contour in enumerate(bp):
        # move to the starting point of the contour
        bp2.moveTo(bp[ci][0][0])
        # loop through the segments
        for si, segment in enumerate(contour):
            # make a list for our new segment
            # this will contain the distorted points
            newSegment = []
            # loop through the points
            for point in segment:
                # unpack
                x, y = point
                # get a random number near x and y
                nx = randint(int(x)-v, int(x)+v)
                ny = randint(int(y)-v, int(y)+v)
                # append our new coordinates to the segment
                newSegment.append((nx, ny))
            # if our segment has more than one point, add it as a curve
            if len(segment) > 1:
                bp2.curveTo(*newSegment)
            # otherwise, add it as a line 
            else:
                bp2.lineTo(*newSegment)
        bp2.closePath()

    # move down to the next line
    translate(0, -mySize)
    # draw the second path
    drawPath(bp2)
