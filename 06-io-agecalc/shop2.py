food1_name          = "Pizza"
food1_price         = 75.00
print("do you want ", food1_name, "(yes/no)")
food1_confirm       = input()
#online food order
delivery_free_limit     = 500.00
delivery_cost           = 100.00
client_is_vip           = False
if food1_confirm == 'yes' :
    food1_quantity      = int(input("how many? ")) 
    food1_cost          = food1_price * food1_quantity
    print(food1_name, " x ", food1_quantity, ' = ', food1_cost, "$")
    delivery_wants      = input('dou you want delivery? (yes/no)')
    client_want_delivery    = delivery_wants == 'yes'
    if delivery_wants   == "yes":
        order_cost              = food1_cost
        delivery_free_cost      = order_cost > delivery_free_limit
        delivery_is_free        = client_want_delivery and (client_is_vip or delivery_free_cost)
        delivery_is_free and print('you got free delivery')
        not delivery_is_free and print('you got to pay ', delivery_cost, "for delivery")
        pass
    
    confirm_oreder      = input("do you agree to pay so much money?(yes/no)")
    if confirm_oreder   == 'yes':
        print("Pay your order and enjoy!")
    else:
        print("Purchese aborted")
else:
    print("Purchese aborted")
print("Thank you. You're the best!")