fs = FormattedString('Hello world', font='MinionPro-Regular', fontSize=100)

bp = BezierPath()

bp.text(fs)

r = 2

bp2 = BezierPath()

drawPath(bp)
for contour in bp:
    for segment in contour:
        pointIndex = 0
        for point in segment:
            
            if len(segment) == 1:
                fill(1, 0, 0)
            elif pointIndex >= 2:
                fill(1, 0, 0)
            else:
                fill(0, 1, 0)
            x, y = point
            oval(x-r, y-r, r*2, r*2)
            pointIndex += 1