# make an image object
im = ImageObject('../../assets/black-raspberries.jpg')

# draw text into the image
with im:
    # anything at this indent will be drawn into the image rather than the canvas
    fontSize(172)
    fill(1, 1, .5)
    text('hello world', (0, 0))

# now apply a distortion to the image
im.pinchDistortion((width()/2, height()/2), 200)
newPage(*im.size())

image(im, (0, 0))