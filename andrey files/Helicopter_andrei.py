from os import system
system("cls")
SCALE  = 10

hX = 5
hY = 3

map = "" 
for y in range(SCALE):
    map += str(y) + ".  "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        
        elif hY-2 <= y <= hY+2 and hX-1 <= x <= hX+1 :
            map += "~ " 
        elif hX-2<= x<= hX +2 and hY-1 <= y <= hY+1:
            map += "~ "
        #elif y== hY-1 and x == hX:
        # #   map += "x "  
        #elif y== hY-1 and x == hX+1 :
         #   map += "x "  
        else:
            map += "  "

    map += "\n"                

print(map)