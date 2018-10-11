from getInput import *

def playMadlibs():
    quickEnd = False
    magicColor = False
    magicWord = False
    color1 = getColor("Enter a color: ")
    if color1 == "white":
        quickEnd = True
    elif color1 == "blue":
        print "There once was a pineapple under the sea!"
    elif color1 == "Blue":
        print "SMURF THE SMURF UP"
    elif color1 == "purple":
        magicColor = True
    elif color1 == "black":
        magicWord = True
        
        
        

    friend1 = getWord("Enter a name: ")    
        
        
        
    output = ""
    output += color1
    output += friend1
        
        
        
        
        
        return output



