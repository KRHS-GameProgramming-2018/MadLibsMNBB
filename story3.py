from getInput import *


def playMadlibs():
    adjective1 = getWord("Enter an adjective: ")
    celebrity1 = getWord("Enter a female celebrity name: ")
    pet1 = getPet("Enter a common jungle ani animal: ")
    food1 = getWord("Enter a type of unhealthy food: ")
    god1 = getGod("Enter an olympian: ")



    output = ""
    output+= "Once upon a time, there was a" + adjective1 + "princess by the name of " +celebrity1
    output+= celebrity1 + "lived high in a tower, protected night and day by her fathers massive" + pet1
    output+= "One day, a brave prince attempted to rescue" + celebrity1 + "."
    output+= "The prince charged the castle, wielding a" + food1 + "of unusual size"
    output+= "Out of nowhere, the princes's father, " + god1 + ", roundhouse kicked the charging prince."

