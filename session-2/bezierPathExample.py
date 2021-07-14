# define a bezier path

# by defining the object separately from drawing it to the canvas, we can do things in between

b = BezierPath()
# rather than drawing a rect to the canvas, draw it into a bezier path
b.rect(0, 0, 100, 100)
# now transform the bezier path
# rather than transforming the canvas
b.skew(20)

# nothing is drawn to the canvas until we use the drawPath function
drawPath(b)