font('Megazoid', 200)

myColors = {'red': (1, 0, 0)}


translate(0, -fontDescender())

with savedState():
    fill(*myColors['red'])
    rect(0, 0, width(), fontXHeight())

text('pop latitude', (0, 0))

