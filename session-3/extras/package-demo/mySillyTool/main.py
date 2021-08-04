
Variable([

    dict(name="leftHandleLength", ui="Slider",
            args=dict(
                value=0,
                minValue=-150,
                maxValue=150)),
                
    dict(name="rightHandleLength", ui="Slider",
            args=dict(
                value=0,
                minValue=-150,
                maxValue=150)),
                
    dict(name="myText", ui="EditText") 
    ], globals())


print(dir())

sh = 200
#rightHandleLength = randint(-150, 150)
#leftHandleLength = randint(-150, 150)

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

fill(1, 0, 0)
fontSize(150)
text(myText, (20, 20))