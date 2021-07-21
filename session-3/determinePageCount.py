
myText = FormattedString(' '.join(installedFonts()), fontSize=2)
pageCount = 0
while myText:
    myText = textOverflow(myText, (0, 0, width(), height()))
    pageCount += 1
print(pageCount)