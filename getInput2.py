def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "2" 
            or response == "Two"):
            response = "2"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True              
        else:
            print "Please make a valid choice"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word
    
    
    
def getColor(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        color1 = ["red", "blue", "green", "yellow", "purple", "orange", "black", "pink"]
        goodInput = True
        for character in word:
            if (color1 == "white"):
                output += "THE END"
                print showMenu()
                break
            # else "Invalid color"
                goodInput = False
                
    return word
                

def isSwear(word):
    swearList = ["poop",
                "piss", 
                "crap", 
                "schlong", 
                "Dinglemister", 
                ]
    if word in swearList:
        return True
    else:
        return False
        
        
        
        
def getCountry(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        country1 = ["Afghanistan", "Iraq", "Isreal", "Syria", "Iran", "Saudi Arabia", "Qatar", "Jordan", "Yemen", "United Arab Emirites", "Cypris", "Kuwait", "Bahrain"]   
        goodInput = True
        for character in word:
            if character not in country1:
                print "not good enough"
                goodInput = False
                break
                
                
    return word
