from os import system
from time import sleep
from random import randint
rx = 10
bx = -9 
by = -6 
tx = 2
ty = 5
score = 0 

option  = ""
while option!='x':
    system("cls")
    for y in range(1,21):
        for x in range(1,21):
            if x == rx and y ==20 :
                print("R", end=" ")
            elif x == bx and y == by:
                print("|", end=" ")
            elif x == tx and y == ty:
                print("O", end=" ")
            else:
                print(".",end=" ")
        print()
    ############ Bulet movet up ############### 
    if by != -6:
        if bx == tx and by == ty:
            tx = randint(1,20)
            ty = randint(1,15)
            by = -1

            score +=20
            continue
        by -=1 
        sleep(0.02)
        continue  
    print("\nScore: ",score)
 
    ############ define inputs ###############
    option = input("\n a = left, d = right, space for shoot\n x to quit.\n Introduce your command and hit enter\n >>> ")
    if option == 'a' and rx >1:
        rx -=1
    if option == 'd'and rx <20:
        rx +=1
    if option == ' ': #### Shoot request
        bx = rx
        by = 19
        score -= 5
    bx = rx