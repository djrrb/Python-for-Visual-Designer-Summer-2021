# make a random polygon 
# numPoints is optional (default: 5)
def randomPolygon(x, y, w, h, numPoints=5):
    # make an empty list
    pointList = []
    # add a certain number of points
    for pt in range(numPoints):
        # for each point, append a random x and y to the list
        pointList.append(
            (
                randint(-100, 100), 
                randint(-100, 100)
            )
        )
    # unpack the list and feed it to polygon
    polygon(*pointList)
        
# move to the center
# draw our random polygon
translate(width()/2, height()/2)
randomPolygon(0, 0, 200, 200, numPoints=100)
