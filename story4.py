from getInput import *

def playMadlibs():
    quickEnd = False
    magicColor = False
    magicWord = False
    floatingWord = False
    color1 = getColor("Enter a color: ")
    friend1 = getWord("Enter a name: ")
    
    
    if color1 == "white":
        quickEnd = True
    elif color1 == "blue":
        print "There once was a pineapple under the sea! "
    elif color1 == "Blue":
        print "SMURF THE SMURF UP"
    elif color1 == "purple":
        magicColor = True
    elif color1 == "black":
        magicWord = True
    elif color1 == "yellow":
        floatingWord = True
    else:
        pass
        
        
    if magicColor:
        output = " \nThere can only be one"  

    elif magicWord:
        output = friend1   [::-1]
    
    elif floatingWord:
        import antigravity
    else:
        
        
        
        output = ""
        output += "What is your favorite color? " + color1 + " "
        output += friend1 + " says " + color1
        output += ""
            
        
        
        
        
    return output



