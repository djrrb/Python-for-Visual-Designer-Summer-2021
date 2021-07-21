# call an image

# move to the center
translate(width()/2, height()/2)
# loop 10 times
for i in range(10):
    # draw our image
    image('hello-world.pdf', (0, 0))    
    # rotate the canvas
    rotate(-45)