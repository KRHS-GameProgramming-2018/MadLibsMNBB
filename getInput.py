def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "2" 
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
            print "Please make a valid choice boi"
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
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            goodInput = False
    
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
        colors = ["red", "white", "blue", "Blue", "green", "yellow", "purple", "orange", "black", "pink"]
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
            goodInput = False
            
        if word in colors:
            goodInput = True
        else:
            print "Invalid selection"
            goodInput = False
    return word

def getCountry(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        countries = ["Afghanistan", 
                     "Iraq", 
                     "Isreal", 
                     "Syria",
                     "Iran",
                     "Saudi Arabia",
                     "Qatar", 
                     "Jordan",
                     "Yemen", 
                     "United Arab Emirites", 
                      "Cypris",
                      "Kuwait", 
                      "Bahrain"]   
        goodInput = True
        if word not in countries:
            print "That Ain't it chief"
            goodInput = False
            
                
                
    return word

def getSnacc (prompt) :
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "who snacks on that?"
        return word
        
        
def warCry1 (prompt) :
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word) :
            goodInput = True
        else:
            print "that's a weak war cry"
        return word
        
def getFriend(prompt, name):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not word == name:
            goodInput = True
        else:
            print "Get more friends"
    return word
    
    
def getObject(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Try Again"
    return word


def getGod(prompt) :
    goodimput = false
    while not goodimput:
         word = raw_input(prompt)
         gods = ["Zues", "Hades", "Dionysus", "Hermes", "Ares", "Hera", "Demeter", "Hestia", "Posiden", "Athena", "Apollo", "Artemis"]
         if not isSwear(word):
            goodInput = True
         else:
            print "Watch yo language"
        
         if word in gods:
            goodimput = true
         else:
            print "That ain't no god"
            goodimput = false
    return word
        




def isSwear(word):
    swearList = ["poop",
                "piss", 
                "crap", 
                "schlong", 
                "dinglemister",
                "fuck,"
                "shit,"
                "ass,"
                "asshole,"
                "bitch,"
                "bastard,"
                "bitch tits,"
                "slut,"
                "dick,"
                "cock,"
                "penis,"
                "scrotum,"
                "vagina,"
                "whore,"
                "balls,"
                
                 
                ]
    if word in swearList:
        return True
    else:
        return False

