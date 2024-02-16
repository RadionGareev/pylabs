#HW 4 lift  to first and last floor  bug 


dir_up      = +1
dir_down    = -1
dir_stop    = 0
b_floors    = 12
b_roof_et = int(b_floors)
b_roof      = True
b_parking   = True
lift_floor  = 3
lift_open   = False
lift_dir    = dir_up
human_floor = 3
h_in_lift   = True
from os import system
system("cls")

if b_roof:
    print("---|-----|----")
    print(" R |     |   ")

   
for floor in range(b_floors,0,-1):
   
   
    if floor == lift_floor + 1 and h_in_lift:
        #l = '  ^  '
        if lift_dir == dir_up:
            l = '  ^  '
        elif lift_dir == dir_down:
            l = '  v  '
    elif floor==lift_floor :
        l = "|   |"
    else:
        l = '     '
   
    if b_roof == False and b_roof_et == floor:
        b = "-----"
    elif floor == lift_floor -1:
        b  = "|___|"
    elif floor == lift_floor:
        b  = "|^^^|"
    else:
        b   ="     "        
    print(f"---|{b}|----")

    if floor==human_floor and not h_in_lift:
        h = " H  "
    elif floor==human_floor and h_in_lift and floor==lift_floor:
        l = "| H |"    
    else:
        h = "    "


    print(f"{floor:^3}|{l}|{h}")

if b_parking:
    print("---|     |----")
    print(" P |     |   ")
    print("---|-----|----")
if b_parking == False:
    print("---|-----|----")