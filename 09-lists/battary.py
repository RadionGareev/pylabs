from os import system
fill = 4
system("cls")


print("+--+--+")
for n in range(5):
    if int((100-fill)/20) == n:
        print("+-----+  <<< charge = ", fill, " %")
    print("|     |")
print("+-----+")