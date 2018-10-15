from getInput import *


def playMadlibs():
    adjective1 = getWord("Enter an adjective: ")
    celebrity1 = getWord("Enter a female celebrity name: ")
    pet1 = getWord("Enter a common jungle animal: ")
    food1 = getWord("Enter a type of unhealthy food: ")
    god1 = getGod("Enter an olympian: ")
    rodent1 = getWord("Enter a plural rodent name: ")
    object1 = getWord("Enter a common city object: ")
    verb1 = getWord("Enter a verb ending in ing: " )
    
    output = ""
    output+= "Once upon a time, there was a " + adjective1 + " princess by the name of " +celebrity1
    output+= ". " + celebrity1 + " lived high in a tower, protected night and day by her father's massive " + pet1 + "."
    output+= " One day, a brave prince attempted to rescue " + celebrity1 + "."
    output+= " The prince charged the castle, wielding a " + food1 + " of unusual size. "
    output+= "Out of nowhere, the princes's father, " + god1 + ", roundhouse kicked the charging prince."
    output+= god1 + " called down a plague of " + rodent1 + "."
    output+= "The brave price retreated, tripping over a wild " + object1
    output+= "The swarm of " + rodent1 + " surrounded the panicing prince, " + verb1 + " him in seconds."
    output+= " Not today, " + celebrity1 + ". "
    output+= " THE END"


    return output
