# define an image object
im = ImageObject('../assets/black-raspberries.jpg')

# apply filters
im.sepiaTone()
im.kaleidoscope()

# get width and height of image
imW, imH = im.size()
# shorthand for
#imW = im.size()[0]
#imH = im.size()[1]

# make a page the size of the image
newPage(*im.size())

# draw the image in the bottom left corner
image(im, (0, 0))