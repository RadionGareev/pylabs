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
#bonus HW:
sorted_guests = sorted(guests)
print('\n\nNot repeated list:\n')
for guest in range(len(sorted_guests)):
    print(guest+1, '.', sorted_guests[guest])
print()

