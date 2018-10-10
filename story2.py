from getInput import *

def playMadlibs():
    # friend1 = getWord("Enter a Name: ")
    # numAnimals = getNumber("Enter a number: ", 2, 10)
    # animals1 = getWord("Enter a pluaral animal name: ")
    # color1 = getColor("Enter a color: ")
    # friend2 = getWord("Enter a Name: ")
    country1 = getCountry("Enter a Middle Eastern Country: ")
    animal1 = getWord( "Enter an animal: ")
    bodypart1 = getWord( "Enter an appropriate body part: ")
    object1 = getWord( "Enter a household object: ")
    noise1 = getWord( "Enter a common sound heard in New York City: ")
    object2 = getWord( "Enter a musical instrament: " )
    bodypart2 = getWord("Enter an appropriate body part: ")
    
    
    output = ""
    output += "One day, I stumbled into " + country1 + "," 
    output += " Where I suddenly came face-to-face with a wild " + animal1 + "."
    output += " I stood frozen there, my eyes glued to the animals massive " + bodypart1 + "."
    output += "Thinking fast, I grabbed the nearest weapon, a " + object1 + "."
    output += "The " + animal1 + " charged, releasing a war cry that sounded like a " + noise1 +"."
    output += " I perried the first blow with my trusty " + object2 
    output += " and stabbeded the monster with its own " + bodypart2
    output += "The moster reeled and I stood triumphantly, waving my shiny " + object1 + " high in the air."
    output += "THE END"
    
    
    
    return output

