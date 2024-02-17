from os import system
option = ''
robo_x = 5
over = False
hp = 100 
gmap = [' ',' ',' ','⚠',' ','x',' ',' ',' ','⚠', ]
while option!="x":
    system("cls")
    ######### PRINT THE MAP
    print ("-"*20)
    for i in range(len(gmap)):
        print(gmap[i], end=" ")
    print()
    print("-"*20)
    for i in range(len(gmap)):
        print(i,end=" ")
    print("\n\nHP: ", hp, ' %')
    print("\n Controls:\n a=left, d=right, x=exit\n")
    ########### Game over:
    if hp<1:
        over = True
    if over == True:
        print('Game Over !\n')
        break    
    ########### CONTROLS:
    option = input(">>> ")
    if option == 'd' and robo_x < len(gmap)-1:
        gmap[robo_x] = ' '
        robo_x +=1
        if gmap[robo_x] == '⚠':
            gmap[robo_x] = '☠'
            hp -= 50
        else:
            gmap[robo_x]= 'x'
    if option == 'a' and robo_x > 0:
        gmap[robo_x] = ' '
        robo_x -=1
        if gmap[robo_x] == '⚠':
            gmap[robo_x] = '☠'
            hp -= 50
        else:
            gmap[robo_x]= 'x'
    elif option=='x':
        print('game over')