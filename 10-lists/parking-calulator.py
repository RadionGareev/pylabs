from os import system
p       = ["Mercedes", None, "BMW",None, None, "Toyota", "BMW","Mercedes"]
total   = len(p)
free    = 0
car_num = {}
car_name= "1"
system('cls')
print("On this parking we have:")
print("N\t Name\t Q\t  \n")
for i in range(len(p)):
    if p[i] == None:
        free += 1
    if p[i] != None:
        if p[i] in car_name:

            continue
        else:
 #          car_num.append(p[i])
           car_num +=1

           #print(p[i]) 
#for c in range(len(car_name)):
print(car_name)
#print(c+1,"\t", car_name,)
#print(car_name)
print("Parking (free/total):", free, "/", total, "places.\n", "total Car models: ", car_num )
