# import the libraries we will use
import csv
import os
from datetime import datetime

inch = 72
margin = 96
pageDimensions = 8.5*inch, 11*inch
textFont = 'Courier New'
boldFont = 'Courier New Bold'
textFontSize = 11
textLineHeight = 15
amountWidth = 100

# open the CSV in read mode with UTF-8 unicode encoding
with open('Orders - Sheet1.csv', 'r', encoding='utf-8') as database:
    # read the CSV with the python CSV reader
    # https://docs.python.org/3/library/csv.html
    orders = csv.reader(database)
    
    # loop through the rows in the database
    # use the enumerate function to get a row index (“row”)
    # in addition to the row contents (“order”)
    for row, order in enumerate(orders):
        # the first row of the CSV is special because it contains the column headers
        # lets keep those as a variable
        if row == 0:
            columnHeaders = order
            # use the continue statement to keep
            # the loop going without doing any more
            # processing of the first row
            continue
        
        # for all other rows, collect the data in a dictionary
        # this will map row headers to their value
        data = {}
        # loop through all the column headers and add the corresponding index of the CSV row
        for keyIndex, key in enumerate(columnHeaders): 
            data[key] = order[keyIndex]

        # now we have a dictionary where we can use the column header to call on the row value
        print(data)
            
        # is the order paid? 
        # we will treat the invoice differently if so
        paid = data['Paid'] == 'TRUE'
        
        # make a new drawing so everybody gets their own invoice
        newDrawing()
        # make a new page for the invoice
        newPage(*pageDimensions)

        # determine the marginWidth for later use
        marginWidth = width() - margin*2


        # if the order is paid, draw a watermark
        if paid:
            with savedState():
                font('Impact', 400)
                fill(None)
                stroke(1, 0, 0, .15)
                strokeWidth(3)
                # I just eyeballed the position
                translate(170, 45)
                rotate(45)
                text('PAID', (0, 0))


        # move to the top left of the margin area
        translate(margin, height()-margin)

        # draw the title
        with savedState():
            titleText = 'INVOICE'
            # measure the text at 1pt high
            font('Impact', 1)
            tw, th = textSize(titleText)
            # now that we have the width of the text at 1pt
            # we determine the font size based what fits the 
            # margin width
            titleSize = marginWidth/tw
            fontSize(titleSize)
            lineHeight(titleSize)
            text(titleText, (0, -titleSize+20))
            
        # move our "cursor" below the title
        translate(0, -titleSize)
        # and add a little margin
        translate(0, -margin/2)

        # my info is hardcoded into the invoice
        # add the address
        address = """
Conway, MA USA
+1 555-555-5555
david@djr.com"""

        addressfs = FormattedString(font=textFont, fontSize=textFontSize, lineHeight=textLineHeight)
        addressfs.append('DAVID JONATHAN ROSS', font=boldFont)
        addressfs.append(address, font=textFont)
        addressHeight = textLineHeight * ( len(address.split('\n')) + 2)

        translate(0, -addressHeight)
        textBox(addressfs, (45, 0, marginWidth, addressHeight))

        # add a "from" label
        labelfs = FormattedString('From:', font=textFont, fontSize=textFontSize, lineHeight=textLineHeight)
        textBox(labelfs, (0, 0, 50, addressHeight))

        # Now get the customer info from the CSV
        customerInfo = FormattedString('', font=textFont, fontSize=textFontSize, lineHeight=textLineHeight)
        customerInfo.append(data['Customer'].upper(), font=boldFont)
        customerInfo.append('\r'+data['Address'], font=textFont)
        # draw it in a second column
        textBox(customerInfo, (220+45, 0, marginWidth, addressHeight))
        # and a “to” label
        labelfs = FormattedString('To:', font=textFont, fontSize=textFontSize, lineHeight=textLineHeight)
        textBox(labelfs, (220, 0, 50, addressHeight))

        # convert the date string into a datetime object
        # this way we can interpret the date and display it how we want
        # https://docs.python.org/3/library/datetime.html
        theDate = datetime.strptime(data['Date'], '%Y-%m-%d')
        # now convert the date to a string in a friendlier format
        displayDate = theDate.strftime('%B %d, %Y')
        
        # make a formatted string to display the invoice number and date
        orderTitle = FormattedString(font=boldFont, fontSize=textFontSize, lineHeight=textLineHeight)
        orderTitle.append('\nINVOICE N°:\t' + data['Invoice Number'] + '\nDATE:\t\t' + displayDate)
        
        text(orderTitle, (0, 0))
        
        # move the cursor down again
        translate(0, -textLineHeight)
        
        # make a table with our items
        itemsAmountTitle = FormattedString(font=boldFont, fontSize=textFontSize, lineHeight=textLineHeight)
        # add tabs so we can use '\t' to go to our second column
        itemsAmountTitle.tabs((marginWidth-amountWidth, 'left'))
        itemsAmountTitle.append('ITEMS\tAMOUNT')
        
        # move the cursor down
        translate(0, -textLineHeight*4)
        text(itemsAmountTitle, (0, 0))

        # draw a line
        with savedState():
            strokeWidth(.75)
            stroke(0)
            line((0, -textFontSize), (marginWidth, -textFontSize))

        # make a formatted string to collect our product list
        # start it empty and set the same tabs
        productInfo = FormattedString(font=textFont, fontSize=textFontSize, lineHeight=textLineHeight)
        productInfo.tabs((marginWidth-amountWidth, 'left'))

        # i set up the CSV so that multiple products are split with a semicolon
        # of course there are less hacky ways to do this, but that’s a database design problem, not a python problem ;-)
        for productData in data['Product'].split(';'):
            # if products have a subtotal price, those are separated by an underscore. again, hacky but oh well.
            productItems = productData.split('_')
            # if a price is listed, add "US $"
            if len(productItems) > 1:
                itemCost = 'US $ '+productItems[-1]
                itemName = ' '.join(productItems[:-1])
            else:
                # otherwise the item has a name and the cost is blank
                itemName = productData
                itemCost = ''
            
            # now append them to the formatted string, separated by a tab and followed by a new line
            productInfo.append(itemName+'\t'+itemCost+'\n')
    
        # add the total
        # do slightly different things if the invoice is paid
        if paid:
            totalDisplay = 'TOTAL PAID'
        else:
            totalDisplay = 'TOTAL TO PAY'

        # add the total cost from the invoice
        productInfo.append('%s\tUS $ %s' %(totalDisplay, str(data['Cost'])), font=boldFont, lineHeight=textLineHeight*2.3)

        # determine the height of the formatted string
        # and draw it in a text box
        productInfoHeight = textSize(productInfo)[1]
        translate(0, -textLineHeight-productInfoHeight)
        textBox(productInfo, (0, 0, marginWidth, productInfoHeight))

        # add another line to separate total from products
        with savedState():
            strokeWidth(.75)
            stroke(0)
            line((0, textLineHeight*2), (marginWidth, textLineHeight*2))

        if not paid:
            translate(0, -textLineHeight*3)
            font(textFont)
            textBox('Payment for this invoice is due within 60 days.', (0, 0, marginWidth, 30))

        # make a folder called invoices in this directory
        # but only if it doesn't exist
        if not os.path.exists('invoices'):
            os.makedirs('invoices')
        # add each invoice
        fileName = 'invoice-'+str(data['Invoice Number'])+'-'+data['Customer'].replace(' ', '')+'.pdf'
        saveImage('invoices/'+fileName)