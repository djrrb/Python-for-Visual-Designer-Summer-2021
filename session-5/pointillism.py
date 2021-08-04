# define the image as an object
im = ImageObject("https://i.ytimg.com/vi/PB5FosTwM8s/maxresdefault.jpg")

# make the canvas size the size of an image
newPage(*im.size())

# define how many rows and columns we want for the grid
cols, rows = 50, 30

# determine the cell size
cellWidth = width()/cols
cellHeight = height()/rows

# make our grid
# loops for rows and cols
for row in range(rows):
    for col in range(cols):
        # get our x and y coordinates
        x = col * cellWidth
        y = row * cellHeight
        # "eyedrop" the color from our (x, y) coords
        theColor = imagePixelColor(im, (x, y))
        # set that as the fill color
        fill(*theColor)
        # print the coords
        print(x, y)
        # draw an oval
        oval(x, y, cellWidth, cellHeight)
        
