#HW for 9_18 video 
from os import system
lenght = int(input("Introdude lenght: "))
weight = int(input("introdude weight: ")) 
system ("cls")
size = lenght*weight
n = 1
print()
while n <= size:
    print("+", end=" ")
    if n % lenght ==0:
        print()
    n+=1
print()