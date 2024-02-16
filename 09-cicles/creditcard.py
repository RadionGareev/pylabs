from os import system
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
    print("card number fount")
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
print("hello mr. ", client["name"])
print(client["acc"])
introduce_want = input("would you like to supply card amount?\n (y/n)>>> ") =="y"
if introduce_want:
    int_amount = int(input("how much money  would you like to introduce? \n >>> "))
    int_amount *= 100 # turn cants to $
client["balance_amount"] += int_amount
print("your amout is: ", client["balance_amount"]/100, "$")
client["card_number"] = "1111-2222-3333-4444"
client["card_pin"] = "1234"
