# saved state practice

# make some changes to the canvas state
# these will apply generally
translate(50, 50)
fill(1, 0, 0)
font('Times')
tracking(100)

with savedState():
    # make some more changes to the canvas
    # within savedState()
    # the general settings will still apply but these will override them
    font('Verdana')
    fontSize(100)
    fill(0)
    translate(200, 200)
    text('hello world', (0, 0))
# when we dedent, we return to the original settings
oval(-50, -50, 100, 100)
fontSize(300)
text('hello', (0, 0))