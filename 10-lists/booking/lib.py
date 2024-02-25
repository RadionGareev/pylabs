from os import system
quantity =0
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
    print ("4. Manage")
    print ("0. Exit")
    try:
        option = int(input("choose >>> "))
    except:
        print("only digints")


def renderDestinations():
    for i in range(len(destinations)):
        print(f"{destinations[i]:>20} {prices[i]:10.2f}")
    input("hit enter to continue...")

def renderPrices():
    for price in prices:
        print(price)
    input("3hit enter to continue...")

def searchDestination():
    global quantity
    destination = input("enter destination name: ")
    found = destination in destinations
    if found:
        print(f"destination'{destination}' is available\n")
        for i in range(len(destinations)):
            if destination == destinations[i]:
                print("The price for " f"{destination} is {prices[i]:10.2f}\n")
        #HW3
        # ask  for tickets Q
        # calculate total cost
        # ask for confiramtion
        try: 
            quantity = int(input("how many tickets would you like to buy?\n>>> "))
            summ = quantity*prices[i]
            agree = input(f"The total price would be: {summ} $.\nDo you agree  to by it? (y/n)\n>>> ") == "y"
            if agree:
                print("\nThank you!\n")
            else:
                print("\nTry again\n")
        except:
            print("only digits")

        

    else:
        print(f"destination'{destination}' is UNavailable")
    input("hit enter to continue...")