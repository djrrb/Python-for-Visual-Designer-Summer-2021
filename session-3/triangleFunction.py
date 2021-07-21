# make a function that doesn’t already exist
def triangle(x, y, w, h):
    print(x, y, w, h)
    # make a polygon
    polygon(
        # lower left
        (x, y), 
        # half way across, all the way up
        (x+w/2, y+h), 
        # all the way across, back to the bottom
        (x+w, y) 
        )
        
# use our triangle function
stroke(0)
strokeWidth(10)
triangle(0, 0, 500, 500)
fill(1, 0, 0)
triangle(500, 500, 100, 100)