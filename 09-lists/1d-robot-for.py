from os import system
roboX   = 5
roboHP  = 100
LENGHT  = 18
option  = "" 
bombX   = 11
bombX2   = 17
roboBT  = 100
roboHeal = 1
roboHeal2 = 12
score    = 13
score2   = 14
zareadca = 9
roboScore = 0
#game loop"
while True:
    ################ Draw map ################
    system("cls")
    print("\n")

    for x in range (1 , LENGHT +1):
        if x == roboX:
            print("〠", end=" ")
        elif x == bombX:
            print("💣", end=" ")
        elif x == roboHeal:
            print("💚", end=" ")
        elif x == zareadca:
            print("🔋",end=" ") 
        elif x== score:
            print("💰",end=" ")       
        else:
            print(".",end=" ")
    print("\n")
    print("HP:", roboHP,"%, ", "Batt:", roboBT,"%, Score:", roboScore)
    ################ Draw map ################
    option = input(">>> a = left, d=right : \n" )
    ################  MOVE  ##################
    if option   == "a" and roboX > 1:
        roboX -=1
    if option   =="d" and roboX < LENGHT:
        roboX +=1
    if roboX == bombX:
        roboHP -= 89
        bombX = 200
    if roboX == roboHeal:
        roboHP += 5
        roboHeal = 200
    if roboX == score:
        roboScore +=5000
        score = 300
    roboBT -= 1  ### battery going low
    if roboX == zareadca:
        roboBT += 10
        zareadca = 200
    if option   == "x":
        system ("cls")
        print("Thank you for playing! ")
        break


    ################  MOVE  ##################