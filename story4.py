from getInput import *

def playMadlibs():
    quickEnd = False
    color1 = getColor("Enter a color: ")
    if color1 == "white":
        quickEnd = True
    elif color1 == "blue":
        print "There once was a pineapple under the sea!"
    elif color1 == "Blue":
        print "SMURF THE SMURF UP"
