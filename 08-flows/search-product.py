#    list of products
p_name      = ["laptop", "PC", "netbook", "smartphone"]

#   prices
p_price     = [    2000, 3500,      1500,        2500 ]

#   availability
P_instock   = [False,True,True,False]
# input phase

name        = input("enter the product name you would like to buy:\n")

#   check operation

if name in p_name:
    idx = p_name.index(name)
    print("the price is: ", p_price[idx])
    if P_instock[idx] ==False:
        print("but it is in out of stock. sorry :(")
else:
     print("we don't have this product")