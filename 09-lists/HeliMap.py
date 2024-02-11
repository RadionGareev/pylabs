from os import system
system("cls")
SCALE  = 10 
try:
    hX = int(input("inroduce x coordinates: \n >>> "))
    hY = int(input("inroduce y coordinates: \n >>> "))
except:
    quit("introduce only digits from 2 to 8")
if hX >= 9 or hY >= 9 or hX <= 1 or hY <= 1: 
    quit("introcue  from 2 to 9")

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        elif (x == hX-1 and y == hY) or (x == hX-2 and y == hY) or (x == hX+1 and y == hY) or (x == hX+2 and y == hY) or (x == hX-2 and y == hY) or (x == hX and y == hY +1) or (x == hX and y == hY-1)or (x == hX+1 and y == hY +1) or (x == hX-1 and y == hY-1) or (x == hX+1 and y == hY -1) or (x == hX-1 and y == hY+1) :
            map += "x "
        else:
            map += "  "

    map += "\n"                

print(map)