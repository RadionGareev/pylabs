from os import system
seats = [0,0,1,2,0,0,0,1]
option = -1
from time import sleep
while option!=0:
    free_seats = len(seats)
    for pi in range(len(seats)):
        if seats[pi] !=0:
            free_seats -= 1
    system('cls')
    print()
    for pi in  range(len(seats)):
        print("",pi+1,"", end=" ")
    print()
    for pi in range(len(seats)):
        if seats[pi]==1:
            print("|-|", end=" ")
        elif seats[pi]==2:
            print("|+|", end=" ")
        else:
            print("| |", end=" ")
    print("\n\nFree seats: ", free_seats)
    print("\n")

    print("MENU: ")
    print("1. Book ")
    print("2. Buy")
    print("3. Cancel booking")
    print("0. EXIT ")
    print("----------------")
    try:
        option = int(input( ">>> "))
    #HW2 check condition, boundaries and free place
        if option ==1:
            try:
                place = int(input("whitch place? "))
                if place in range(len(seats)+1):
                    if seats[place-1]==0:
                        seats[place-1]=1
                        print("done")
                    elif seats[place-1]==1:
                        print("This plase is already booked!")
                    elif seats[place-1]==2:
                        print("This plase is sold!")
                else:
                    print("No such place.")
            except:
                print("only digits")
            sleep(1)
        elif option ==2:
            try:
                place = int(input("whitch place? "))
                if place in range(len(seats)+1):
                    if seats[place-1]==0:
                        #seats[place-1]=1
                        print("This place is not booked yet. You should book it  before buy it.")
                        sleep(3)
                    elif seats[place-1]==1:
                        print("you just bought place nuber ", place+1, " congratulations!" )
                        seats[place-1]=2
                        sleep(3)
                    elif seats[place-1]==2:
                        print("This plase is sold!")
                        sleep(1)
                else:
                    print("No such place.")
            except:
                print("only digits")
            sleep(1)
        if option ==3:
            try:
                place = int(input("whitch place? "))
                if place in range(len(seats)+1):
                    if seats[place-1]==0:
                        
                        print("It wasn't booked yet")
                        sleep(2)
                    elif seats[place-1]==1:
                        seats[place-1]=0
                        print("Booking canceled!")
                        sleep(1)
                    elif seats[place-1]==2:
                        print("This plase is sold! You can't ask  for that")
                        sleep(3)
                else:
                    print("No such place.")
            except:
                print("only digits")
            sleep(1)    
    except:
        print("Wrong input!")
        sleep(0.2)
    #HW3 add buy, cancel,  check only if booked 
    