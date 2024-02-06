PIN_DOOR_1      = "0123"
PIN_DOOR_2      = "4321"
# user input and check 1
pin_door_1      = input("Enter first pin:\n ")
lock_1_open     = pin_door_1 == PIN_DOOR_1 # bool
if lock_1_open:
    print("I'm in the Building")
    pin_door_2      = input("Enter second pin:\n ")
    #check PIN_2
    lock_2_open     = pin_door_2 == PIN_DOOR_2 # bool
    if lock_2_open:
        print("I'm in the FLAT")
    else:
        print("Wrong PIN_2")
else:
    print("Wrong PIN_1")

