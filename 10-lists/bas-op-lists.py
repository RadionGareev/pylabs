guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]
from os import system
system('cls')
commonlist = guests_1+guests_2+guests_3
guests = []
print('Common list:\n')
for guest in range(len(commonlist)):
    print(guest+1, '.', commonlist[guest])
      
for guest in range(len(commonlist)):
    if commonlist[guest] not in guests:
        guests.append(commonlist[guest])
print('\n\nNot repeated list:\n')
for guest in range(len(guests)):
    print(guest+1, '.', guests[guest])
print()

