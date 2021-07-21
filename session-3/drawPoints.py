# feed a formatted sting to a bezierpath
# visualize the points of the text

# define a radius for our points
r = 4


# make a formatted string
fs = FormattedString('Hello world', font='MinionPro-Regular', fontSize=200)

# make a bezier path
bp = BezierPath()

# feed the formatted string into the bezier path as text
bp.text(fs, (20, 20))

# draw the path 
# (same as running "create outlines" on text)
drawPath(bp)

# now that we have drawn the path,
# draw the points

# a bezierPath is a list of contours. loop through them
for contour in bp:
    # a contour is a list of segments
    for segment in contour:
        # keep track of our points
        pointIndex = 0
        # loop through our points
        for point in segment:
            # the color depends on the kind of point
            # if the segment has one point, it's a line. make it red
            if len(segment) == 1:
                fill(1, 0, 0)
            # if the segment is 2 or greater, it must be the corner point on a curve segment. Make it red too.
            elif pointIndex >= 2:
                fill(1, 0, 0)
            # Otherwise, make it green! 
            else:
                fill(0, 1, 0)
            
            # unpack our point into x and y
            x, y = point
            # draw a oval centered on the point
            oval(x-r, y-r, r*2, r*2)
            
            # increment our point index
            pointIndex += 1
            
