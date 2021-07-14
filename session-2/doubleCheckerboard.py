rs = 50

# loop through y
for y in range(0, height(), rs):
    # loop through x
    for x in range(0, width(), rs):
        # set the fill randomly
        fill(random(), random(), random())
        # rather than drawing one rectangle in our grid
        # draw two, one in the lower left of the grid cell (x, y) and one in the upper right (x+rs/2, y+rs/2)
        rect(x, y, rs/2, rs/2)
        rect(x+rs/2, y+rs/2, rs/2, rs/2)