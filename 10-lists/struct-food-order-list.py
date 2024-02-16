food_names  = ["Pizza","Salad","Soup","Cola"]
food_price  = [75.00, 45.00, 15.00, 10.00]
food_quant  = [2,1,2,2]
total_cost  = 0
from os import system
system("cls")
print("N\t Name\t price\t Q\t Cost\t \n")
for i in range(len(food_names)):
    total = food_quant[i]*food_price[i]
    total_cost += total
    
    print(i+1,"\t", food_names[i], "\t", food_price[i], "\t", food_quant[i], "\t", total)
    # total = fp[1]*fq[2]
print("\nTotal cost: ", total_cost, "$\n")