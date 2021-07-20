def triangle(x, y, w, h):
    print(x, y, w, h)
    polygon(
        (x, y),
        (x+w/2, y+h),
        (x+w, y)
        )
        
def randomPolygon(x, y, w, h, numPoints=5):
    pointList = []
    for pt in range(numPoints):
        pointList.append(
            (
                randint(-100, 100), 
                randint(-100, 100)
            )
        )
    polygon(*pointList)
        
translate(width()/2, height()/2)
randomPolygon(0, 0, 200, 200, numPoints=100)
