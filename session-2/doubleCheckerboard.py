for y in range(0, 1000, 100):
    for x in range(0, 1000, 100):
        fill(random(), random(), random())
        rect(x, y, 50, 50)
        rect(x+50, y+50, 50, 50)