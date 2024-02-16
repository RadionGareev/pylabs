from os import system
from time import sleep
client_name                            = "John Doe"
client_acc                             ="01234567789012"
client_balance_amount                  = 100000 # 1000.00         
client_balance_currency                = "USD"
int_amount                             = 0
# client dictionary 1
client  =  {
    "name"              : "John Doe",
    "acc"               : "01234567789012",
    "balance_amount"    : 100000,
    "balance_currency"  : "USD",
    "card_pin"          : "2",
    "card_number"       : "1"
}
system("cls")



# authenticate the clienti
check_card_number = input("hello sir.\n please itroduce  your card number:\n >>>")
if check_card_number == client["card_number"]:
    print("card number found")
else:
    quit("no such card, sorry")

for pin in range(3):
    check_pin =input("itroduce  your card pin:\n >>>")
    if check_pin == client["card_pin"]:
        print("pin is correct")
        break
    else:
        print("wrong pin, try again")
if check_pin != client["card_pin"]:
        quit("pin wrong, card is bloked")
system("cls")
# interactive Menu 

while True:
    system("cls")
    print("hello mr. ", client["name"])
    print("your account number is: ", client["acc"])
    try:
        menu = int(input("\n MENU: \n 1 for check balance \n 2 to change the pin \n 3 to supply amount \n 4 to get some money. \n 0 to quit \n your choice? >>> "))
        if menu == 1:
            print(" your balance is : ", client["balance_amount"]/100, "$")
        if menu == 2:
            new_pin = input("introduce the new pin: \n >>>")
            client["card_pin"] = new_pin
            print("your new pin now is : ", client["card_pin"])
        if menu == 3 :
            int_amount = int(input("how much money  would you like to introduce? \n >>> "))
            int_amount *= 100 # turn cants to $
            client["balance_amount"] += int_amount
            print("your amout is: ", client["balance_amount"]/100, "$")
        if menu == 4 :
            int_amount = int(input("how much money  would you like to get? \n >>> "))
            int_amount *= 100 # turn cants to $
            client["balance_amount"] -= int_amount
            print("your amout is: ", client["balance_amount"]/100, "$")
        if menu == 0:
            print("thank you, bye!")
            break 
        else:
            something_else = input("would you like something else?(y/n) ") == "y"
            if something_else:
                pass
            else:
                print("thank you, bye!")
                break 
                
    except:
        print("Only digits! try again")
        sleep(2)

    

     
