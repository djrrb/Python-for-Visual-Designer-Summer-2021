# draw a recursive tree

# set some constants
branchLength = 190
# this is how many levels deep we will let this go
# recursion will go on forever otherwise, no fun
maxDepth = 8

# our branch function will draw a line and then call itself to draw two lines at the end of it
def branch(depth):
    # draw a line
    line((0, 0), (0, branchLength))
    # move to the top of the line
    translate(0, branchLength)
    # check to make sure we’re not in too deep
    if depth < maxDepth:
        # save the state
        with savedState():
            # rotate and scale
            rotate(-20)
            scale(.8)
            # call branch() from within branch
            # increase the depth
            branch(depth+1)
        # do it again for the second branch 
        with savedState():
            rotate(20)
            scale(.8)
            branch(depth+1)

# now we’re out of the function and in the main script

# remember defining the function doesn't actually draw anything
# but because the function is recursive, calling it once will draw the whole tree

# set our formatting
stroke(0)
strokeWidth(10)
lineCap('round')
# move the center with a little margin on the bottom
translate(width()/2, 50)

# draw the tree!
branch(0)