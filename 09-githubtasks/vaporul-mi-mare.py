from os import system
system("cls")
try:
    cx = int(input("Hi. introduce small ship coordonate from 1 to 40: \n >>> "))
    if cx  not in range(1,41):
        quit()
except:
    quit("wrong input")

big_ship = cx
for x in range(1,41):
    if x == big_ship:
        print( "wWw", end="" )
    else:
        print( "~", end="" )
