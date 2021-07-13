
# make a loop for each page of a multipage document
for page in range(10):
    newPage(1000, 1000)
    fill(1)
    rect(0, 0, 1000, 1000)
    for y in range(0, 1000, 100):
        for x in range(0, 1000, 100): 
            print(x)
            fill(random(), random(), random(), 1)
            oval(x, y, 100, 100)

saveImage('grid.gif')
