#HW 4 lift  to first and last floor  bug 

###########   define variables ############
dir_up      = -1
dir_down    = +1
dir_stop    = 0
b_floors    = 9
#b_roof_et   = True
b_roof      = True
b_parking   = True
lift_floor  = 3
lift_open   = True
lift_dir    = dir_stop
lift_call   = False
human_go    = False  ## lift target
human_floor = int(input("with floor is the human? \n>>> "))
h_in_lift   = False
h_go_out    = False
from os import system
from time import sleep
###########   define variables ############


############  Start  While cicle ############
while True:   
    lift_call = input("call the lift (y/n): ") == "y"
    if lift_call:
        if not h_in_lift:
            human_go = human_floor
        else:
            human_go = int(input(" where to go? "))
    else:
        human_go == lift_floor
    lift_open = False
    if lift_floor < human_go:
        speed = +1
        lift_dir = dir_up
    if lift_floor > human_go:
        speed = -1
        lift_dir = dir_down
    if lift_floor ==    human_go:
        speed = 0
        lift_dir = dir_stop

        ######### Animation ###########
    while True:
        if not dir_stop:
            lift_floor += speed
            if lift_floor == human_go:
                lift_open = True
                lift_dir = dir_stop


        sleep(.1)
        system("cls")
        ############# print  the roof
        if b_roof:
            print("---|-----|----")
            print(" R |     |   ")
        ############## Drawing this Building 
        for floor in range(b_floors,0,-1):
            a = '     '
            c = '     '
            t = '     '
            s = ' '
            if floor == lift_floor +1:
                if lift_dir == dir_down:
                    a = '  v  '
                elif lift_dir == dir_up:
                    a = '  ^  '
                elif lift_dir == dir_stop and lift_open:
                    a = ' < > '
            elif floor == lift_floor:
                a = '|   |'
                t = '|---|'
                if h_in_lift:
                    a = '| H |'
            elif floor == lift_floor -1:
                t = '|---|'
            elif floor == human_floor:
                if not h_in_lift:
                    s = 'H'
            print(       f'---|{t}|---')
            print(f'{floor}:^3|{t}|---')

        ########## draw roof ##########
            if b_roof == False and b_roof == floor:
                b = "-----"    
            elif floor == lift_floor -1:   #### bottom of the lift
                b  = "|___|"
            elif floor == lift_floor:
                b  = "|^^^|"
            else:
                b   ="     "        
            print(f"---|{b}|----")     #### top of the lift 
        ##########  draw Lift  ######
            if floor==human_floor:
                if h_in_lift==False:
                    h = " H  "
                if h_in_lift and floor == lift_floor:
                    l = "| H |"
                    h = "    "    
                if floor == lift_floor + 3 and h_in_lift:
                        l = ' < > '
    #        elif lift_call:
    #            while lift_floor < human_floor:
    #                lift_dir = dir_up
    #                break
    #            while lift_floor> human_floor:
    #                lift_dir = dir_down
    #                break
            
            elif lift_dir == dir_up:
                l = '  ^  '
                #lift_floor += 1
                #sleep(.5)
            elif lift_dir == dir_down:
                l = '  v  '
                #lift_floor -= 1
                #sleep(.5)
            elif floor==lift_floor :
                l = "|   |"
            elif h_go_out and h_in_lift==False and human_go==lift_floor:
                l = "|   |"
            else:
                l = '     '
                h = "    "
        #########  Print  each Floor #############
            print(f"{floor:^3}|{l}|{h}")        ########### important
        #########   Print Parking  ###############
        if b_parking:
            print("---|     |----")
            print(" P |     |   ")
            print("---|-----|----")
        if b_parking == False:
            print("---|-----|----")
        #########  call lift Menu ################
        if human_floor==human_go and h_go_out:
            sleep(1)
            break
        if h_in_lift==False:    
            menu = input("c to call the lift \n  x to exit \n >>> ")
        if menu == "x":
            break
        if menu == "c":     
            #lift_call=True
            if lift_floor == human_floor and h_in_lift:
                menu = int(input("where  you want to go? \n choose  1-9 or x  to exit \n >>> "))
                if not h_in_lift:
                    human_go = menu
                    lift_floor = human_go
                    human_floor = human_go
                    h_in_lift = False
                    h_go_out = True
                if human_go == "x":
                    break
            lift_floor = human_floor
            sleep(.5)
            h_in_lift = True
        if h_go_out:
            h_in_lift= False


################ End While cicle ###############
