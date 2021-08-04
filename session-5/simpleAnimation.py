dotCount = frames = 30

colWidth = width()/dotCount


for frame in range(frames):
    newPage()
    frameDuration(1/20)
    translate(0, height()/2)
    y = 0
    for dot in range(dotCount):
        
        cycleY = cos(2*pi*dot/dotCount)
        y = cycleY * height()/2
        print(y)
        if frame == dot:
            fill(1, 0, 0)
            d = 40
            
        else:
            fill(0)
            d = 20
        oval(-d/2, y-d/2, d, d)
        translate(colWidth, 0)
        
saveImage('dots.gif')