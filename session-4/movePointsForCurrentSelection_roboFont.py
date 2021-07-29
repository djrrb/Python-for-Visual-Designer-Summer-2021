# this script is meant to be run in RoboFont’s drawbot extension
# this means it can access functions that are part of drawbot
# AND functions that are part of robofont (CurrentFont(), CurrentGlyph(), etc)
# https://github.com/typemytype/drawBotRoboFontExtension

# FontParts is used in RoboFont to express the font and its contents as a python object
# https://fontparts.robotools.dev/en/stable/objectref/index.html

# get the current font as the variable f
f = CurrentFont()
# the current selection is a list of glyph names
# loop through that list

for glyphName in f.selection:
    # the font is kind of like a dictionary mapping glyph names to glyph objects
    # get the glyph object by calling it from the font by name
    glyph = f[glyphName]
    # i don’t think the undo works but what the heck
    glyph.prepareUndo('mess up points script')
    
    # loop through all the countours in the glyph
    for contour in glyph:
        # loop through each segment in the contour
        for segment in contour:
            # loop through each point in teh segment
            for point in segment:
                # if the point type is either a line or a curve
                if point.type in ['line', 'curve']:
                    # move the point x and y 
                    point.x += randint(-20, 20)
                    point.y += randint(-20, 20) 
    glyph.performUndo()     
    # update our window so we can see the changes
    # sometimes this happens automatically but sometimes not
    glyph.update()
    # make the glyph a random color
    glyph.mark = random(), random(), random(), 1
    # since we can use drawbot we can also draw the glyph to our drawbot  cnavas
    fill(None)
    strokeWidth(2)
    stroke(1, 0, random())
    drawGlyph(glyph)