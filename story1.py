from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    color1 = getColor("Enter a color: ")
    friend2 = getWord("Enter a Name: ")
    
    
    
    
    output = ""
    output += "One day I ran over my friend, " + friend1
    output += ". Suddenly " + friend1
    output += " said that they saw a " + color1 + " light " 
    output += "I quickly grabbed a "
    
    
    
    
    
    return output
