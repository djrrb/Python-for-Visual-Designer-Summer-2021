
im = ImageObject("https://i.ytimg.com/vi/PB5FosTwM8s/maxresdefault.jpg")
#image(im, (0, 0))

cols, rows = 50, 50
cellWidth = width()/cols
cellHeight = height()/rows
for row in range(rows):
    for col in range(cols):
        x = col * cellWidth
        y = row * cellHeight
        fill(*imagePixelColor(im, (x, y)))

        print(x, y)
        oval(x, y, cellWidth, cellHeight)