def triangle(x, y, w, h):
    print(x, y, w, h)
    polygon(
        (x, y),
        (x+w/2, y+h),
        (x+w, y)
        )
        
def pentagon(x, y, w, h):
    pointList = []
    for pt in range(5):
        pointList.append(
            (
                randint(-100, 100), 
                randint(-100, 100)
            )
        )
    polygon(*pointList)
        
pentagon(0, 0, 200, 200)
stroke(0)
strokeWidth(10)
line((0, 0), (100, 100))
triangle(0, 0, 500, 500)
fill(1, 0, 0)
triangle(500, 500, 100, 100)