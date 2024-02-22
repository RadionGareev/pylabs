#HW1 create prices.txt
#HW2 create function read prices.

from os import system
option = 0 
running = True
destinations = []
prices = []
def readDestinations():
    global destinations
    file = open(r"D:\Python\pylabs\10-lists\booking\dest.txt", "r")
    lines = file.readlines()
    for line in lines:
        destinations.append(line.strip("\n"))
    file.close()
def readDPrices():
    global prices
    file = open(r"D:\Python\pylabs\10-lists\booking\prices.txt", "r")
    lines = file.readlines()
    for line in lines:
        price = float(line.strip("\n"))
        prices.append(price)
        #print(prices)
        #input("wait here")
    file.close()
###################         Define functions
def renderMenu():
    global option
    system("cls")
    print("MAIN MENU:")
    print ("1. Search destination")
    print ("2. Show destinations")
    print ("3. Show price")
    print ("0. Exit")
    option = int(input("choose >>> "))

def renderDestinations():
    for destination in destinations:
        print(destination)
    input("hit enter to continue...")

def renderPrices():
    for price in prices:
        print(price)
    input("3hit enter to continue...")

def searchDestination():
    destination = input("enter destination name: ")
    found = destination in destinations
    if found:
        print(f"destination'{destination}' is available")
    else:
        print(f"destination'{destination}' is UNavailable")
    input("hit enter to continue...")
###################   HOC (High Operate Code)
readDestinations()
readDPrices()
while running:
    renderMenu()
    if option==1:
        searchDestination()
    if option==2:
        renderDestinations()
    if option==3:
        renderPrices()
    if option==0:
        running=False
        print("Bye!")

