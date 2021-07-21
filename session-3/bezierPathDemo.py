# make a shape using BezierPath

# shape height
sh = 200
# determine the length of each handle randomly
rightHandleLength = randint(-150, 150)
leftHandleLength = randint(-150, 150)

# define a bezier path
bp = BezierPath()
#  move to my starting point
bp.moveTo((0, 0))
# straight line across
bp.lineTo((width(), 0))
# straight line up
bp.lineTo((width(), sh))
# make my curve
bp.curveTo(
    (width(), sh+rightHandleLength), # right handle
    (0, sh-leftHandleLength), # left handle
    (0, sh) # upper left point
    )
# draw the path
drawPath(bp)