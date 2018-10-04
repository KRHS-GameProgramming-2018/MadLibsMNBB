from getInput import *

def playMadlibs():
    quickEnd = False
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    # animals1 = getWord("Enter a pluaral animal name: ")
    color1 = getColor("Enter a color: ")
    if color1 == "white":
        quickEnd = True
    else:
        snacc1 = getSnacc ("Enter a snacc: ")
        friend2 = getWord("Enter a Name: ")
        animals1 = getWord("Enter a pluaral animal name: ")
    
    
    
    
    output = ""
    output += "One day I ran over my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw a " + color1 + " light " 
    if quickEnd:
        output += "\nTHE END"
    else:
        output += "I quickly grabbed a " + snacc1
        output += "This proved to be a poor choice when a rampant" + animals1
    
    
    
    
    
    
    return output
