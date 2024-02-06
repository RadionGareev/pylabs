#ask for student grade
try:
    grade       = int(input("introduce your grade:\n"))
except:
    exit("introduce only digits")
#Estimate and print
if grade > 10 or grade < 1:
    exit("you wrote a wrong grade, it shoulbe from 1 to 10!")
elif grade > 7 and grade <=10:
    print("good grade") 
elif grade >4 and grade <=7:
    print("not bad!")

else:
    print("Bad!")
