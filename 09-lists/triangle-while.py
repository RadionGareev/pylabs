from os import system
system("cls")

h =int(input("Introduce height of the reiangle in pixels: "))
calc = h-1      
n = 0
while n < h:
    print("   "*(calc-n), "+  " * ((n+1)*2-1))
    n+=1
print()

### 2=3, 3=5, 4=7, 5=9, 6=11, 7=13,8=15,9=17