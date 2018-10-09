from getInput import *

def playMadlibs():
    quickEnd = False
    friend1 = getWord("Enter a Name: ")
    # numAnimals = getNumber("Enter a number: ", 2, 10)
    # animals1 = getWord("Enter a pluaral animal name: ")
    color1 = getColor("Enter a color: ")
    if color1 == "white":
        quickEnd = True
    else:
        snacc1 = getSnacc ("Enter a snacc: ")
        animals1 = getWord("Enter an animal name: ")
        friend2 = getFriend("Enter a Name: ", friend1)
        object1 = getObject("Enter a throwable object: ")
        warCry1 = getWord("Enter the war cry of a warrior: ")
    
    
    
    
    output = ""
    output += "One day I ran over my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw a " + color1 + " light " 
    if quickEnd:
        output += "\nTHE END"
    else:
        output += "I quickly grabbed a " + snacc1
        output += ". This \nproved to be a poor choice when a rampant " + animals1
        output += " screeched and hollered a war cry fit for a warrior. "
        output += friend2 + " Threw " + object1 + "at the monkey, "
        output += "letting loose a valiant '" + warCry1 + "'"
        output += "/nThe monkey was pronounced dead on the scene"
    
    
    
    
    
    
    return output
