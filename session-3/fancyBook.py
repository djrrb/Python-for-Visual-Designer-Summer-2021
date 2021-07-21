def myShape(sh):
    hsl = 950
    rightHandleLength = randint(-hsl, hsl)
    leftHandleLength = randint(-hsl, hsl)
    bp = BezierPath()
    # this is my starting point
    bp.moveTo((0, 0))
    # straight line across
    bp.lineTo((width(), 0))
    # straight line up
    bp.lineTo((width(), sh))
    # make my curve
    bp.curveTo(
        (width(), sh+rightHandleLength),
        (0, sh-leftHandleLength),
        (0, sh)
        )
    drawPath(bp)
    

def drawBackground():
    sh = 200
    for i in range(10):
        fill(random(), 0, 1, .2)
        myShape(sh)
        sh += 100



myText = FormattedString(fontSize=14)
for fontName in installedFonts()[:1000]:
    if fontName[0] != '.':
        myText.append(fontName+' ', font=fontName, fill=(random(), random(), random()))


pageCount = 0

while myText:
    
    


    newPage('LetterLandscape')
    drawBackground()

    margin = 60
    marginWidth = width()-margin*2
    marginHeight = height()-margin*2
    fill(1)
    rect(margin, margin, marginWidth, marginHeight)
    innerMargin = 50
    
    myText = textBox(
        myText,
        (margin+innerMargin, margin+innerMargin, marginWidth-innerMargin*2, marginHeight-innerMargin*2)
    )
    pageCount += 1
    fill(0)
    font('Verdana')
    fontSize(20)
    text(str(pageCount), (margin, margin))
    
