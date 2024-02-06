PIN_DOOR_1      = "0123"
PIN_DOOR_2      = "4321"

# user input

pin_door_1      = input("Enter first pin:\n ")
pin_door_2      = input("Enter second pin:\n ")

#check keys
lock_1_open     = pin_door_1 == PIN_DOOR_1 # bool
lock_2_open     = pin_door_2 == PIN_DOOR_2 # bool

#show the result

if lock_1_open and lock_2_open:
    print("I'm in the FLAT")
else:
    print("wrong pin")
