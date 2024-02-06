from time import sleep
from os import system
e_what  = input("Eevent type: ")
e_where = input("Event location: ")
e_when  = input("Event time: ")

system("clear")
sleep(3)

print("\n"*2)
print("-"*40)
print("attention")
print("You have a", e_what,e_where, 'at', e_when, "hours")