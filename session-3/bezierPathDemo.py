sh = 200
rightHandleLength = randint(-150, 150)
leftHandleLength = randint(-150, 150)

bp = BezierPath()
# this is my starting point
bp.moveTo((0, 0))
# straight line across
bp.lineTo((width(), 0))
# straight line up
bp.lineTo((width(), sh))
# make my curve
bp.curveTo(
    (width(), sh+rightHandleLength),
    (0, sh-leftHandleLength),
    (0, sh)
    )
drawPath(bp)