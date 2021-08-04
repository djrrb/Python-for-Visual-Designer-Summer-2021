# here are some functions to help us interpolate
def lerp(start, stop, amt):
	return float(amt-start) / float(stop-start)
def norm(value, start, stop):
	return start + (stop-start) * value
def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)


frames = 60
# define a path to the font, this can be installed or a path to a font file
fontPath = '../../assets/CondorVariable-VF.ttf'

# set the font
font(fontPath)
# query the variations of the current font
variations = listFontVariations()
# loop through them
for variation in variations:
    print(variations[variation])
    for infoItem in variations[variation]:
        print(infoItem)

# get the min and max values of specific axes
# variations['wght'] gets the info dict
# variations['wght']['minValue'] gets the value within the info dict
wghtMin = variations['wght']['minValue']
wghtMax = variations['wght']['maxValue']

italMin = variations['ital']['minValue']
italMax = variations['ital']['maxValue']

wdthMin = variations['wdth']['minValue']
wdthMax = variations['wdth']['maxValue']

# loop through the frames
for frame in range(frames):
    newPage()
    frameDuration(1/15)
    # draw background
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    # draw our animating curve
    with savedState():
        translate(width()/frames/2, height()/2)
    
        # track x movement in this variable
        x = 0
        # loop through each frame to draw the sin wave
        for frameDisplay in range(frames):
            # get the size of the dot, depending
            # current frame’s dot is big
            # first frame’s dot is tiny
            # all other frames are small
            if frameDisplay == frame:
                d = 40
            elif frameDisplay == 0:
                d = 10
            else:
                d = 20
            # our progress through the sequence is frameDisplay/frames
            # get the sine of our progress multiplied by a full circle (2*pi)
            # this gives us a value between -1 and 1 that we can map to a sine wave
            yprogress = sin(2*pi * frameDisplay/frames)
            # get our actual y value by multiplying our progress by half the height
            # we multiply it by half because the sine wave goes above and below zero
            # so in either direction it’s half the height
            y = yprogress * height()/2
            # draw our dot
            stroke(0, 1, 0)
            fill(None)
            oval(x-d/2, y-d/2, d, d)
            # advance to the next column to draw our next dot
            x += width()/frames
    
    # now do the same calculations, but for the current page/frame
    yprogress = sin(2*pi * frame/frames)
    # use the remap function to map this progress onto the font’s weight axis range
    wghtValue = remap(yprogress, -1, 1, wghtMin, wghtMax)

    # do the same for width, but use cosine instead
    wdthProgress = cos(2*pi * frame/frames)
    wdthValue = remap(wdthProgress, -1, 1, wdthMin, wdthMax)
    
    # italic can be the same as weight
    italValue = remap(yprogress, -1, 1, 0, 1)

    # make a formatted string 
    # fontVariations are defined as a dictionary
    # mapping the 4 letter axis keyword to the numeric value
    fs = FormattedString('hi', 
        font=fontPath, 
        fontSize=600, 
        align="center", 
        fontVariations={
            'wght': wghtValue, 
            'wdth': wdthValue, 
            'ital': italValue
        }
    )
    
    # draw the text box
    # subtract from the full height so the text is vertically centered
    # this is a bit hacky but it works
    textBox(fs, (0, 0, width(), height()-200))
        
saveImage('animated-text.gif')