# set up a dictionary of features
# mapping 4 letter feature keys to True/False values
# list of features:
# https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae

myFeatures = {
    'smcp': True,
    'onum': True,
    }

# set up a dictionary of palettes
# the key is the palette name
# the value is another dictionary with color names and values
myPalettes = {
    'darkMode': {'foreground': (0, 0, 0), 'background': (1, 1, 1)},
    'lightMode': {'foreground': (1, 1, 1), 'background': (0, 0, 0)}
    }

# draw a page for each mode
for mode in myPalettes.keys():
    newPage()
    # set the background color
    # use the mode name to select the mode within the dictionary
    # and use 'background' to get the background color from that
    # use * to unpack the values
    fill(*myPalettes[mode]['background'])
    rect(0, 0, width(), height())
    # set the opentype features
    # use ** to unpack the dictionary
    # this is the same as openTypeFeatures(smcp=True, onum=True)
    openTypeFeatures(**myFeatures)
    # now set the foreground color and draw the text
    fill(*myPalettes[mode]['foreground'])
    fontSize(200)
    font('MinionPro-Regular')
    text('hello 123', (50, 50))