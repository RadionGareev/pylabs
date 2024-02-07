###########      Variables       ############
rx = 12 
ry = 18 

###########      Draw MAP        ############
for x in range(1,21):
    for y in range(1,21):
        if y==ry and x ==rx:
            print("👴",end="")
        elif x==rx -1 and y==ry:
            print("+",end=" ")
        elif x==rx +1 and y==ry:
            print("+",end=" ")
        elif x==rx and y==ry-1 :
            print("+",end=" ")
        elif x==rx and y==ry +1:
            print("+",end=" ")
            ##### HW1 #######
        elif x==rx -1 and y==ry-1:
            print("+",end=" ")
        elif x==rx +1 and y==ry+1:
            print("+",end=" ")
        elif x==rx-1 and y==ry+1 :
            print("+",end=" ")
        elif x==rx+1 and y==ry -1:
            print("+",end=" ")
        else:
            print(".",end=" ")
    print()
###########      Sensors         ############

###########      Actions         ############
