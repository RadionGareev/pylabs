from os import system
from time import sleep
system("cls")

friends = []
while len(friends) < 100:
    system('cls')
    name = input("Add friend name: \n or hit enter to vieiw results \n >>> ")
    if name in friends:
        print(" you already have friend ", name , " mentioned, plese try another one.")
        sleep(1)
        continue
    if name == "":
        break
    friends.append(name)
print("you have ", len(friends), "friends")
for i in range(len(friends)):
    print(" ", i, ">>", friends[i])
