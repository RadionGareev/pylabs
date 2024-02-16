from os import system
system("cls")
people = ["Jony","Mary","Francis","Fernando"]
print("People in list:\n")
for i in range(len(people)):
    print(i+1, people[i])
want = input("would you like to renum some of them(y/n)?\n>>> ")=="y"
if want:
    select_who = int(input("wich number? \n>>> "))-1
    if select_who > len(people) or select_who < 0:
        quit("Write correct number! " )
    select_where = int(input("where you would like to replece it(number)? \n>>> "))-1
    if select_where > len(people) or select_where < 0 or select_where == select_who:
        quit("Write correct number! " )    
else:
    quit("Okay, bye!")                
temp        =people[select_who]
people[select_who]   =people[select_where]
people[select_where]   =temp
print("After people in list:" )
for i in range(len(people)):
    print(i+1, people[i])