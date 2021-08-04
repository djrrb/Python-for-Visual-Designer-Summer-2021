# interpolation functions
# Released by DJR under the BSD license 
def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate using a value between 0 and 1
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value

def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    """
    Re-maps a number from one range to another.
    """
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)

# set some constants
dotCount = frames = 30
colWidth = width()/dotCount

# for each frame make a new page and set the duration
for frame in range(frames):
    newPage()
    frameDuration(1/20)

    # start our x at 0
    # it will be used for the dots
    x = 0
    
    for dot in range(dotCount):
        
        cycleY = cos(2*pi*dot/dotCount)
        cycleItalic = sin(2*pi*dot/dotCount)
        y = cycleY * height()/2 + height()/2
        # if our dot corresponds to the current frame
        # make it red and bigger
        # also draw some text
        if frame == dot:
            fill(1, 0, 0) # red
            d = 40 # bigger
            # set the font
            font('../assets/CondorVariable-VF.ttf', 200)
            # get the weight value based on the cos cycle
            # get the italic value based on the sin cycle
            wghtValue = remap(cycleY, -1, 1, 200, 900)
            italicValue = remap(cycleItalic, -1, 1, 0, 1)
            # set the font variations
            fontVariations(wght=wghtValue, ital=italicValue)
            # print the weight value
            print(wghtValue)
            # draw the textbox
            # fudge the height so it's vaguely centered
            textBox('hello', (0, 0, width(), height()/1.6), align="center")
        else:
            # if our dot doesn't represent the current frame
            # make it small and black 
            fill(0)
            d = 20
    
        # draw the dot
        oval(x-d/2, y-d/2, d, d)
        # move x to the next column
        x += colWidth

# at the very end, save our image
# dedent all the way so it only happens once 
saveImage('dots.gif')