# make a little book of all installed fonts

# define a shape
# see waves.py file for full comments
def myShape(sh):
    hsl = 950
    rightHandleLength = randint(-hsl, hsl)
    leftHandleLength = randint(-hsl, hsl)
    bp = BezierPath()
    bp.moveTo((0, 0))
    bp.lineTo((width(), 0))
    bp.lineTo((width(), sh))
    bp.curveTo(
        (width(), sh+rightHandleLength),
        (0, sh-leftHandleLength),
        (0, sh)
        )
    drawPath(bp)
    
# make a background out of multiple myShapes
def drawBackground():
    sh = 200
    for i in range(10):
        fill(random(), 0, 1, .2)
        myShape(sh)
        sh += 100


# start with an empty formatted string
# we wil fill it with contents
myText = FormattedString(fontSize=14)
# loop through the first 1000 items in installedFonts
for fontName in installedFonts()[:500]:
    if fontName[0] != '.':
        myText.append(fontName+' ', font=fontName, fill=(random(), random(), random()))


# keep track of the number of pages
pageCount = 0

# make a while loop
# this will keep looping until myText is empty
while myText:
    # make a new page
    newPage('LetterLandscape')
    # draw our random background
    drawBackground()

    # define margins
    margin = 60
    innerMargin = 50
    # determine the dimensions of our white box
    marginWidth = width()-margin*2
    marginHeight = height()-margin*2
    innerMarginWidth = marginWidth-innerMargin*2
    innerMarginHeight = marginHeight-innerMargin*2
    # draw the white box
    fill(1)
    rect(margin, margin, marginWidth, marginHeight)
    
    # draw our text box with equal margins inside the white box
    # textBox() will return the overflow text to myText
    # this whittles it down each time until there is nothing left 
    myText = textBox(
        myText,
        (margin+innerMargin, margin+innerMargin, innerMarginWidth, innerMarginHeight)
    )
    
    # increment the page count
    pageCount += 1
    
    # draw a folio in the lower left corner
    fill(0)
    font('Verdana')
    fontSize(10)
    text('Page '+str(pageCount), (margin+10, margin+10))
    
