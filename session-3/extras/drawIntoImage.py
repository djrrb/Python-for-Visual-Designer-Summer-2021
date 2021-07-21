# make an image object
im = ImageObject('../../assets/black-raspberries.jpg')

# draw text into the image
with im:
    # anything at this indent will be drawn into the image rather than the canvas
    fontSize(172)
    fill(1, 0, 0)
    text('hello world', (0, 0))

# now apply a distortion to the image
im.pinchDistortion((width()/2, height()/2))
newPage(*im.size())

# draw the same text that we drew into the image
fontSize(172)
fill(0, 1, 0)
text('hello world', (0, 0))

image(im, (0, 0))