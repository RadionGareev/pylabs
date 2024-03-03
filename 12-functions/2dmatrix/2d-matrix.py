from os import system

def printStar():
    print('*', end=' ')
def printStarRow(w):
    for i in range(w):
        printStar()
    print()
def printStarRect(w,h):
    if w >0 and h >0:
        for i in range(h):
            printStarRow(w)
    else:
        print('Dimension cannot be negative!')
system('cls')
printStarRect(16,9)