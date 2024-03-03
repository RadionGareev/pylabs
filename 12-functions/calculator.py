from os import system
system("cls")
def ii(wich):
    print("Enter", wich, "integer: ", end="")
    return int(input())
a=ii('first')
b=ii('second')
try:
    op = input("Chose operation ( * / + -  **)\n>>>")
except:
    quit("Only integers!")
res = 0
if op =="+":
    res = a+b
elif op =="*":
    res= a*b
#HW1:
elif op =="-":
    res= a-b
elif op =="/":
    res= a/b
elif op =="**":
    res= a**b 
else:
    quit("wrong operation try again")

print("result: ", res)