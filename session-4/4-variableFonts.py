# make a dictionary mapping axis names to axis values
# these will be our defaults
# https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg
myVariations = {
    'ital': 1,
    'wdth': 50
    }

# set the font and font size
fontSize(140)
font('../assets/CondorVariable-VF.ttf')

# we will loop through the weight axis
# use listFontVariations() to query the font for its axes
# select the weight axis, and within it, the minimum value
# convert it to an integer because that’s what range() likes
minValue = int(listFontVariations()['wght']['minValue'])
maxValue = int(listFontVariations()['wght']['maxValue'])

step = 100

# loop through the axis, skipping 100 values at a time
# add 100 to the max to account for the fact that range() does not include the last number in the range
for wghtValue in range(minValue, maxValue+step, step):
    print('wght', wghtValue)
    # modify the dictionary by adding a weight value
    myVariations['wght'] = wghtValue
    # unpack the variations dictionary
    fontVariations(**myVariations)
    # draw the text
    text('hello 0123', (50, 50))
    translate(0, 114)
    