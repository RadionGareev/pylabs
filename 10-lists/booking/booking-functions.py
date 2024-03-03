#HW1 create prices.txt
#HW2 create function read prices.

from os import system
import lib
system('cls')
###################   HOC (High Operate Code)
lib.readDestinations()
lib.readDPrices()

while lib.running:
    lib.renderMenu()
    if lib.option==1:
        lib.searchDestination()
    if lib.option==2:
        lib.renderDestinations()
    if lib.option==3:
        lib.renderPrices()
    if lib.option==4:
        lib.renderOrder()
    if lib.option==5:
        lib.removeOrder()
    if lib.option==0:
        lib.running=False
        print("Bye!")
    else:
        print("would you like to try one more time?")

