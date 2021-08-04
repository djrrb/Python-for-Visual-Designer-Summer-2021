dots = 10
frames = dots
step = width()/dots
d = 20
translate(0, width()/2)

for frame in range(frames):
    for dot in range(dots):
        x = step * dot
        ycycle = sin(2*pi * dot/dots)
        y = ycycle * height()/2
        oval(x-d/2, y-d/2, d, d)
    
    