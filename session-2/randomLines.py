# set a stroke width universally for the document
strokeWidth(10)

# loop a certain number of times
for i in range(1000):
    # set a random fill color that is 50% transparent
    stroke(random(), random(), random(), .5)
    
    # a line takes two (x, y) touples
    # line((x1, y1), (x2, y2))
    line(
        # tuple 1
        (randint(0, width()), # x1
        randint(0, width())), # y1
        # tuple 2
        (randint(0, width()), # x2
        randint(0, width()))  # y2
        )