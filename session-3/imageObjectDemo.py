im = ImageObject('../assets/black-raspberries.jpg')

im.triangleTile()
im.kaleidoscope()

imW, imH = im.size()
# shorthand for
#imW = im.size()[0]
#imH = im.size()[1]
newPage(*im.size())

image(im, (0, 0))