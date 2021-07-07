# for = python keyword for loop
# x = variable name, can be anything 
# in = connecting to the sequence
# range(0, 10) = give me a sequence of numbers

for y in range(0, 1000, 100):
    for x in range(0, 1000, 100): 
        print(x)
        # fill: red, green, blue, alpha
        fill(random(), random(), random(), 1)
        # cymkFill
        #cmykFill(1, 0, 0, 1)
        # x, y, width, height
        oval(x, y, 100, 100)