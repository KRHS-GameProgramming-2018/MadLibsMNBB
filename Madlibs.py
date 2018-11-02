# 190/200 - PD; Very good. Come of your special getters have an issue where any word will work as long as you don't swear.

from screens import *
from getInput import *
import story1
import story2
import story3
import story4

print showSplash()
raw_input("Press Enter to Start")


go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print "Goodbye and thanks for playing"
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print story2.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
         print story3.playMadlibs()
         raw_input("Press Enter to Continue")
    elif response == "4":
         print story4.playMadlibs()
         raw_input("Press Enter to Continue")
    else:
        print "OMG Got invalid menu option!!!"

