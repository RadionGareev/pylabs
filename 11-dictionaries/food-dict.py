from os import system
order = {
    'client'    :   'John Doe',
    'item'      :   'Salad',
    'quantity'  :   3,
    'price'     :   15.00
}
order['total'] = order['price'] * order['quantity']
#HW1 - 20% discount in case  if more than 7 items
if order['quantity'] >7:
    order['total']*=0.8

system('cls')
print("ORDER for    :", order['client'])
print("Food         :", order['item'])
print("Price x qty  :", order['price'], ' x ', order['quantity'],'\n')
print("Total        :", order['total'])
if order['total'] >300:
    print('You odered more than 300$. You can benefit free delivery.  ')
    order['delivery'] = 'free'
else:
    print('You odered less than 300$. Deelivery will cost 50$.  ')
    order['delivery'] = 50

#HW2
delivery_want = input("\n Do you want delivery? y/n \n>>>")=='y'
if  delivery_want and order['total']>300:
    print(f"you got {order['delivery']} delivery. \n\n\n Total  sum  is: {order['total']} \n Enjoy!")
elif delivery_want and order['total']<300:
    order['total'] = order['total']+order['delivery']
    print(f"You should pay {order['delivery']} $ for delivery. \n\n Total  sum  is: {order['total']} ")
else:
    print(' Got it,  no delivery. Come and take your command')
