# figure out how many pages a text will be WITHOUT drawing it

# get all installed fonts as a string (separated by a space)
fontsAsString = ' '.join(installedFonts())
# add our text to a formatted string
myText = FormattedString(fontsAsString, fontSize=12)

# make a variable to count pages
pageCount = 0
# make a while loop
# make sure that the myText variable gets whittled down
while myText:
    # use textOverflow function to return the overflow of myText
    myText = textOverflow(myText, (0, 0, width(), height()))
    # add to our page count each time
    pageCount += 1
print(pageCount)