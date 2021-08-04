
branchLength = 170
maxDepth = 6
def branch(depth):
    line((0, 0), (0, branchLength))
    translate(0, branchLength)
    if depth < maxDepth:
        with savedState():
            rotate(-20)
            scale(.9)
            branch(depth+1)
        with savedState():
            rotate(20)
            scale(.9)
            branch(depth+1)
    
stroke(0)
strokeWidth(10)
lineCap('round')

translate(width()/2, 50)

branch(0)